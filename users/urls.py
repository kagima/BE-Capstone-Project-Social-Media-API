# users/urls.py
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FollowViewSet  # ✅ Added FollowViewSet import

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = router.urls

