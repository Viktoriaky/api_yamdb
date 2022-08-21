from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_token, sign_up
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

API_VER = 'v1'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet, basename='comments')
router_v1.register('users', UserViewSet, basename='users')
urlpatterns = [
    path('v1/auth/signup/', sign_up, name='auth_signups'),
    path('v1/auth/token/', get_token, name='auth_tokens'),
    path('v1/', include(router_v1.urls))]
