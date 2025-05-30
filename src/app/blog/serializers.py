from rest_framework import serializers

from blog.models import BlogPost, Comment


class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content']
        read_only_fields = ['id']


class BlogPostListSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    class Meta:
        model = BlogPost
        fields = ['id', 'created_at', 'updated_at', 'title', 'comments_count']
        read_only_fields = fields


class BlogPostRetrieveSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        return CommentSerializer(obj.comment_set.all(), many=True).data

    class Meta:
        model = BlogPost
        fields = ['id', 'created_at', 'updated_at', 'title', 'content', 'comments']
        read_only_fields = fields


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'updated_at', 'content']
        read_only_fields = ['id', 'created_at', 'updated_at']
