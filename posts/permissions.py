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

class IsAuthorOrReadOnlyAuthorCanEdit(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method not in permissions.SAFE_METHODS and obj.author == request.user:
            return True
        return obj.author == request.user


class IsAuthorOrReadOnlyUbuntu(permissions.BasePermission):
    message = 'How did you log in on something different than Ubuntu, just use ubuntu douchbag!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.META['DESKTOP_SESSION'] == 'ubuntu':
            return True
        return obj.author == request.user


class IsAuthorOrReadOnlyTime(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        from datetime import datetime
        now = datetime.now().replace(tzinfo=None)
        created = obj.created_at.replace(tzinfo=None)
        time_elapsed = (now - created).total_seconds()

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['PUT', 'PATCH'] and obj.author == request.user and time_elapsed < 30:
            return True
        return obj.author == request.user


class OnlyLocalPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        ip_user = request.META['REMOTE_ADDR']
        return ip_user == '127.0.0.1'


class NotPostman(permissions.BasePermission):
    message = 'Postman not allowed'

    def has_permission(self, request, view):
        user_agent = request.META['HTTP_USER_AGENT']
        return 'Postman' not in user_agent
