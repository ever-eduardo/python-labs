from cgitb import text
from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]