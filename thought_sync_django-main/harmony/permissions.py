from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    


class IsSuperUserOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers to access any object
        if request.user.is_superuser:
            return True
        # Allow users to access their own profile
        return obj.user == request.user


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access only to superusers
        return request.user and request.user.is_superuser