from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from lightful_service.quickstart.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'groups', 'id')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Post
        fields = ('title', 'content', 'created_at', 'user_id', 'updated_at', 'id')