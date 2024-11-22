from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # metodo seguro
            return True
        else:
            # metodos nao seguros
            return obj.colecionador == request.user