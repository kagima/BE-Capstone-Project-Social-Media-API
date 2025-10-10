from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, FeedView  # 👈 import FeedView

# Router for post CRUD
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Add a new path for the feed
urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),  # 👈 new feed endpoint
]

# Include both router URLs and feed URL
urlpatterns += router.urls

