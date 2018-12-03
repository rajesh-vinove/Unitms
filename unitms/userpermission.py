from rest_framework.permissions import BasePermission


class AdminBaseUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if request.user:
            permission_list = [request.user.is_normal_user,request.user.is_admin_user]
            if True in permission_list:
                return True
            else:
                return False



class AdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        
        return request.user and request.user.is_admin_user
