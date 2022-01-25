from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username='tusk', password='sweet_tusk')
        post = Post.objects.create(author=user, title='costam', body='fdsfgagasga')

    def test_post_content(self):
        post = Post.objects.get(pk=1)
        self.assertEqual(post.author.username, 'tusk')
        self.assertEqual(post.title, 'costam')
        self.assertEqual(post.body, 'fdsfgagasga')
