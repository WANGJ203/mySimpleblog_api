from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import index, post_list, post_detail

#post_list, post_detail, PostViewSet, UserViewSet

router = DefaultRouter()

# #### for api_view
urlpatterns = [
    path('', index),
    path('posts/', post_list),
    path('posts/<int:pk>', post_detail),
]

# model_view

# router.register('post_viewset', PostViewSet, 'post_model_viewset')
# # router.register('category', CategoryViewSet, 'category_viewset')
# router.register('users', UserViewSet, "users")
#
# urlpatterns = router.urls
#
# urlpatterns.append(path('', index))
# urlpatterns.append(path('posts/', post_list))
# urlpatterns.append(path('posts/<int:pk>', post_detail))
# urlpatterns.append(path('user_id_search/', User_ID_Search))