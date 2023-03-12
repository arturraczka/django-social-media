"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import DEBUG, STATIC_URL, STATIC_ROOT
from apps.routers import router
from apps.users import urls as user_urls
from apps.posts.views import PostListView , PostViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(user_urls)),
    path('profile/<str:slug>/', PostListView.as_view(), name='profile'),
    path('profile/<str:slug>/<str:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name = 'post'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

