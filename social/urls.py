from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from social import views


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('likes/', views.LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>/', views.LikeDetail, name='like-detail')
])
