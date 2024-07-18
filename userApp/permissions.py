from rest_framework.permissions import BasePermission


class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Regular':
            return True
        return False
