from django.urls import path

from blog.views import BlogPostListCreateView, BlogPostRetrieveView, CommentCreateView

urlpatterns = [
    path('posts', BlogPostListCreateView.as_view(), name='blog-post-list-create'),
    path('posts/<int:pk>', BlogPostRetrieveView.as_view(), name='blog-post-retrieve'),
    path('posts/<int:pk>/comments', CommentCreateView.as_view(), name='comment-create'),
]
