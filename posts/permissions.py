from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request.user)
        print(obj.user) # returns testuser when we could be logged in as ppalancica
        # return True
        return request.user == obj.user
