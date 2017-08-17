from rest_framework import permissions

class IsOwnerOrNotShow(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj.owner == request.user:
            return True
        else:
            return False
