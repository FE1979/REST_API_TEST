from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from social import views


# Routers
router = DefaultRouter()
router.register(r'posts', views.PostDetail)


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
])

urlpatterns += router.urls
