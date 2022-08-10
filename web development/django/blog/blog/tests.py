import email
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.comm",
            password="secret"
        )

        cls.post = Post.objects.create(
            title="A Pretty Good Title",
            author = cls.user,
            body="Nice body content dropped here."
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "A Pretty Good Title")
        self.assertEqual(self.post.body, "Nice body content dropped here.")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A Pretty Good Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")