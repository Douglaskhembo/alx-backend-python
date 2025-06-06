from rest_framework import permissions
from .models import Conversation, Message


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow access only to participants of a conversation.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # For Conversation objects
        if isinstance(obj, Conversation):
            return user in obj.participants.all()

        # For Message objects
        if isinstance(obj, Message):
            if request.method in ['GET', 'PUT', 'PATCH', 'DELETE']:
                return user in obj.conversation.participants.all()

        return False
