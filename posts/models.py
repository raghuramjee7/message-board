from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        # This returns the first 50 chars as the postname in the admin panel.
        return self.text[:50]