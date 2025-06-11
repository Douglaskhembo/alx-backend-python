from django.urls import path
from .views import delete_user, threaded_conversations, view_message_thread, unread_messages

urlpatterns = [
    path('delete-account/', delete_user, name='delete_user'),
    path('threaded/', threaded_conversations, name='threaded_conversations'),
    path('message/<int:message_id>/', view_message_thread, name='message_thread'),
    path('inbox/unread/', unread_messages, name='unread_messages'),

]
