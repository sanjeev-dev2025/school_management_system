from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permissions(self,request,view):
        return request.user and request.user.is_authenticated and request.user.role=="ADMIN"
class IsTeacherUser(BasePermission):
    def has_permission(self,request,view):
        return request.user and request.user.is_authenticated and request.user.role=="TEACHER"
class IsStudentUser(BasePermission):
    def has_permission(self,request,view):
        return request.user and request.user.is_authenticated and request.user.role=="STUDENT"
class IsAdminUserOrTeacher(BasePermission):
    def has_permission(self,request,view):
        return request.user and request.user.is_authenticated and request.user.role=="ADMIN" or request.user.role=="TEACHER" 
