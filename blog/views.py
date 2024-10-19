from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Post
from .serializers import PostSerializers
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAuthor
from django_filters import rest_framework as filters
class UserRegistration(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        """
        Register view and it generate a token key
        ---
        response:
        201:
            description: Register View
        """
        if not username or not password:
            raise ValidationError("Username and password are required.")

        user = User.objects.create_user(username=username, password=password, email=email)
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class PostFilter(filters.FilterSet):
    class Meta:
        model = Post
        '''
        Filter method
        '''
        fields={
            'author': ['exact'],
            'created_at':['exact','gte','lte'],
        }
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=PostFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(author=self.request.user)
        return Post.objects.all()
        """to see all posts"""

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        """create new user"""

    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes=[IsAuthor]
        return super().get_permissions()
        """Put: To replace/update entire resource, Patch: To update specific resource, Delete: To delete record"""