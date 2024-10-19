from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Post
        fields = '__all__'