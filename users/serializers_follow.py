from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise serializers.ValidationError("You cannot follow yourself.")
        return data
