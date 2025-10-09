from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Allow users to see their own data only
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=user.id)


from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Follow
from .serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.all()

    def create(self, request, *args, **kwargs):
        following_id = request.data.get('following')
        try:
            following_user = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == following_user:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=following_user)

        if not created:
            return Response({'message': 'Already following this user'}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


