from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly, IsAuthor
from blog.serializers import PostSerializer, UserSerializer


def index(request):
    return HttpResponse('hello world')


# @csrf_exempt
# def post_list(request):
#     # 1 读取所有对象的列表，一个对象的集合
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     # 2 上传或创建一个对象到对象的集合中
#     if request.method == 'POST':
#         mydata = JSONParser().parse(request)
#         serializer = PostSerializer(data=mydata)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
# #
#
# @csrf_exempt
# # 3 读取单个对象的信息 retrieve
# def post_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return JsonResponse(serializer.data)
# #
#     # 4  更改单个对象的信息，或者update 信息
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(post, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
# #
#     # 5 删除单个对象的信息
#     elif request.method == 'DELETE':
#         post.delete()
#         return HttpResponse(status=204)

# 以上方法只是应用POSTMAN 上面的，我没有一个页面去操作，所以创建页面操作的API#####

@api_view(["GET", "POST"])
def post_list(request):
    # 1 读取所有对象的列表，一个对象的集合
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    # 2 上传或创建一个对象到对象的集合中
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.http.HTTP_400_BAD_REQUEST)


#
#
@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # 3 读取单个对象的信息 retrieve
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    #
    # 4  更改单个对象的信息，或者update 信息
    elif request.method == 'PUT':
        # if request.user == post.author:
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response("You do not have permission ")
    #
    # 5 删除单个对象的信息
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
#
# modle view class
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = (TokenAuthentication,)
    # # permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)
    # permission_classes = (IsAuthenticated, IsAuthor,)
#
#
# # token is not enough for fundamental view methods
# # we need to create our own token
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
