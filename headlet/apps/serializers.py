from django.contrib.auth.models import User, Group
from apps.posts.models import Post
from apps.profiles.models import Profile
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'created_at']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'about', 'avatar', 'follows', 'profile_slug']


class ProfileWithPostsSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['user', 'about', 'avatar', 'follows', 'profile_slug', 'user_posts']