from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from apps.serializers import PostSerializer, ProfileSerializer, ProfileWithPostsSerializer
from apps.posts.models import Post
from apps.profiles.models import Profile


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.none()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        user = self.request.user
        queryset = Post.objects.filter(user_profile__user=user, pk=post_id)
        return queryset


class PostListView(ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def are_users_related(self):
        profile_slug = self.kwargs['slug']
        are_related = Profile.objects.filter(profile_slug=profile_slug,
                                             followed_by__user=self.request.user).exists()
        return are_related

    def get_serializer_class(self):
        if self.are_users_related():
            return ProfileWithPostsSerializer
        else:
            return ProfileSerializer

    def get_queryset(self):
        profile_slug = self.kwargs['slug']
        profile = Profile.objects.filter(profile_slug=profile_slug)

        return profile
