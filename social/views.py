from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Follow
from .serializers import FeedSerializer

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the users this person follows
        following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)
        
        # Get posts from those users, newest first
        posts = Post.objects.filter(user__in=following_users).order_by('-timestamp')

        # Serialize and return them
        serializer = FeedSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

