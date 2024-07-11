from rest_framework.permissions import SAFE_METHODS,BasePermission

from accounts.models import UserType

class IsAdminOrReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True
        # else:
        #     return bool(request.user and request.user.type == UserType.admin.value or request.user.is_staff)
        return True if request.method in SAFE_METHODS else bool(request.user and (request.user.type == UserType.admin.value or request.user.is_staff))
    
