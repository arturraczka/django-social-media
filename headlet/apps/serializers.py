from django.contrib.auth.models import User, Group
from apps.posts.models import Post
from apps.profiles.models import Profile
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name = "apps.users:user-detail")
#
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user_profile', 'body', 'created_at']


# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['user', 'about', 'avatar', 'follows']