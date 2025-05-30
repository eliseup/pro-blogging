from django.db import models
from utils.models import DateAbstractModel


class BlogPost(DateAbstractModel):
    title = models.CharField(max_length=45, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


class Comment(DateAbstractModel):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.content
