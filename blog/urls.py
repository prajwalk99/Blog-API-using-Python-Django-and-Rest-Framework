from django.urls import path
from .views import UserRegistration, PostViewSet
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', obtain_auth_token, name='api-token-auth'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
]