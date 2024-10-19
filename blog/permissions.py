from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
     def IsAuthor(self,request,view,obj):
          return obj.author == request.user