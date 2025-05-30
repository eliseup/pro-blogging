from django.urls import reverse

from rest_framework.test import APITestCase

from blog.models import BlogPost


class BlogTestCase(APITestCase):
    @classmethod
    def create_default_post(cls) -> BlogPost:
        return BlogPost.objects.create(**dict(
            title='Default post',
            content='Content for default post.',
        ))

    @classmethod
    def setUpTestData(cls):
        cls.post = cls.create_default_post()

    def retrieve_default_post(self):
        return self.client.get(
            path=reverse('blog-post-retrieve', kwargs={'pk': self.post.pk})
        )


class BlogViewsTests(BlogTestCase):
    """Test the views of the Blog API."""
    def test_create_post(self):
        response = self.client.post(
            path=reverse('blog-post-list-create'),
            data=dict(title='Post', content='Content'),
        )

        assert response.status_code == 201

    def test_list_posts(self):
        response = self.client.get(path=reverse('blog-post-list-create'))

        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_create_comment(self):
        comment_response = self.client.post(
            path=reverse('comment-create', kwargs={'pk': self.post.pk}),
            data=dict(content='Comment content.')
        )

        post_response = self.retrieve_default_post()
        post_comments = post_response.json()['comments']

        assert comment_response.status_code == 201
        assert post_response.status_code == 200
        assert len(post_comments) == 1

    def test_retrieve_post(self):
        response = self.retrieve_default_post()

        assert response.status_code == 200
        assert response.json()['id'] == self.post.pk
