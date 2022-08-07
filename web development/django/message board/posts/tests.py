from django.test import TestCase
from .models import Post


# Create your tests here.
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a post test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a post test!")