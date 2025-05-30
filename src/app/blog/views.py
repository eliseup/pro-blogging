from rest_framework import generics

from blog.models import BlogPost
from blog.serializers import BlogPostCreateSerializer, CommentSerializer, BlogPostListSerializer, \
    BlogPostRetrieveSerializer


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BlogPostCreateSerializer
        return BlogPostListSerializer


class BlogPostRetrieveView(generics.RetrieveAPIView):
    serializer_class = BlogPostRetrieveSerializer
    queryset = BlogPost.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(blog_post_id=self.kwargs.get('pk'))
