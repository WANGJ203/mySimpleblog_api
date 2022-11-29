from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ## if author is in my permissions.safe method list
        if request.method in permissions.SAFE_METHODS:
            return True
        return object.author == request.user

class IsAuthor(permissions.BasePermission):
    message ="you are not an author"

    def has_permission(self, request, view):
        user_groups = request.user.group.value_list("name",flat=True)
        if "author" in user_groups:
            return True
        return False



