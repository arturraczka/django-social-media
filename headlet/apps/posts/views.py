from django.db.models import F
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView

from apps.serializers import PostSerializer
from apps.posts.models import Post
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model

#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         user = self.request.user
#         if Profile.objects.filter(followed_by=user.profile):
#             queryset = Post.objects.filter(user_profile=user).order_by('-created_at')
#             return queryset

#####

# class PostListView(ListAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         profile_slug = self.kwargs['slug']
#         profile = Profile.objects.get(profile_slug=profile_slug)
#
#         if profile.followed_by.contains(self.request.user.profile):
#             return Post.objects.filter(user_profile=profile).order_by('-created_at')
#
#         return Post.objects.none()


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        profile_slug = self.kwargs['slug']
        profile = Profile.objects.get(profile_slug=profile_slug)

        if self.request.user.profile.followed_by.contains(profile):
            return Post.objects.filter(user_profile=profile).order_by('-created_at')

        return Post.objects.none()