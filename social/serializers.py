from rest_framework import serializers
from .models import Post

# Existing serializer — used for creating/managing posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', 'timestamp']


# New serializer — used for displaying the feed
class FeedSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'username', 'content', 'media', 'timestamp']
