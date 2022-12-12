from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, post_detail, PostViewSet, UserViewSet, CategoryViewSet, User_ID_Search

# post_list, post_detail, PostViewSet, UserViewSet

router = DefaultRouter()

router.register('post_viewSet', PostViewSet, 'post_model_viewSet')
router.register('users', UserViewSet, 'users_viewSet')
router.register('category', CategoryViewSet, 'category_viewSet')

urlpatterns = [
    # for api_view function base view
    path('', index),
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail),
    # model_view
    path('api-auth/', include('rest_framework.urls')),

    path('user_id_search/', User_ID_Search),
]
urlpatterns += router.urls
