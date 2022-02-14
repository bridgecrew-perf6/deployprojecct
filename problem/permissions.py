from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_active and request.user == obj.author
        )