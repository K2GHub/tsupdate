from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
    
# end of IsAdminOrReadOnly 


class IsSuperUserOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow superusers to access any object
        if request.user.is_superuser:
            return True
        # Allow users to access their own profile
        return obj.user == request.user

# end of IsSuperUserOrOwner


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access only to superusers
        return request.user and request.user.is_superuser

# end of IsSuperUser


class IsCreatorOrReadOnly (permissions.BasePermission):
    """
    Custom permission to only allow creators of a Synch to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow SAFE_METHODS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the Synch.
        return obj.creator.user == request.user
    
# end of IsCreatorOrReadOnly


class IsMemberOrReadOnly (permissions.BasePermission):
    """
    Custom permission to only allow creators of a Synch to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow SAFE_METHODS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the creator of the Synch.
        return obj.member.user == request.user
    
# end of IsMemberOrReadOnly




