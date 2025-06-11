from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message
from django.shortcuts import redirect
from django.contrib.auth.models import User

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
    # Get top-level messages for the logged-in user
    messages = Message.objects.filter(receiver=request.user, parent_message__isnull=True) \
        .select_related('sender', 'receiver') \
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
