from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, post_detail, PostViewSet, UserViewSet

# post_list, post_detail, PostViewSet, UserViewSet

router = DefaultRouter()

router.register('post_viewSet', PostViewSet, 'post_model_viewSet')
router.register('users', UserViewSet, 'users')

urlpatterns = [
    # for api_view function base view
    path('', index),
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail),
    # model_view
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += router.urls
