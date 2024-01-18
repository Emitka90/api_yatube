from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
