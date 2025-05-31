from rest_framework import serializers

from blog.models import BlogPost, Comment


class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content']
        read_only_fields = ['id']


class BlogPostListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'created_at', 'updated_at', 'title', 'comment_count']
        read_only_fields = fields


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'updated_at', 'content']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BlogPostRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'created_at', 'updated_at', 'title', 'content', 'comments']
        read_only_fields = fields
