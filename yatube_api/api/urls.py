from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, 'comments')
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
