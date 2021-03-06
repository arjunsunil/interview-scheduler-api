from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is tryig to edit thier own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
