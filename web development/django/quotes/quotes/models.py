from django.db import models


# Create your models here.
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=256)

    def publish(self):
        self.save()
    
    def __str__(self) -> str:
        return self.text
