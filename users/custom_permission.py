from rest_framework.permissions import BasePermission

SAFE_METHOD=('GET','HEAD','OPTIONS')

class IsAdminOrReadOnliy(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHOD:
            return True
        return bool(request.user and request.user.is_staff)