from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'body', 'category']
        # can use fields = '__all__' for all fields
        # fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', ]


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True,
        }}

    # 解决上述方法创建的用户无法登录的问题
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # 创建完新用户可以自动登录,自动生成token
        Token.objects.create(user=user)
        # add use to  a group by group ID
        user.groups.add(1)
        return user
