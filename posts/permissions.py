from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # GET OPTION HEAD - SAFE_METHODS
            return True
        return obj.author == request.user


class IsAuthorOrReadOnlyAdminDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # GET OPTION HEAD - SAFE_METHODS
            return True
        if request.method == "DELETE" and request.user.is_superuser:
            return True
        return obj.author == request.user


# TODO - 3 rozne permissiony na zadanie domowe