from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from .models import Message
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q

def get_all_replies(message):
    replies = list(message.replies.all().select_related('sender', 'receiver'))
    all_replies = []

    for reply in replies:
        all_replies.append(reply)
        all_replies.extend(get_all_replies(reply))  # Recursive fetch

    return all_replies


@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home')


@login_required
def threaded_conversations(request):
    # Get top-level messages where the user is the receiver OR sender
    messages = Message.objects.filter(
        Q(receiver=request.user) | Q(sender=request.user),
        parent_message__isnull=True
    ).select_related('sender', 'receiver') \
     .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'messaging/threaded_conversations.html', {'messages': messages})



@login_required
def view_message_thread(request, message_id):
    message = Message.objects.select_related('sender', 'receiver').get(id=message_id)
    replies = get_all_replies(message)
    return render(request, 'messaging/thread_detail.html', {
        'message': message,
        'replies': replies,
    })


@login_required
def unread_messages(request):
    unread_msgs = Message.unread.unread_for_user(request.user).select_related('sender').only(
        'id', 'sender__username', 'content', 'timestamp'
    )
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_msgs})


@cache_page(60)  # Cache this view for 60 seconds
@login_required
def threaded_conversations(request):
    # Get top-level messages where the user is the receiver OR sender
    messages = Message.objects.filter(
        Q(receiver=request.user) | Q(sender=request.user),
        parent_message__isnull=True
    ).select_related('sender', 'receiver') \
     .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'messaging/threaded_conversations.html', {'messages': messages})
