from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        raise MethodNotAllowed(request.method)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, views, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
