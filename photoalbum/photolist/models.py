from django.db import models

# Create your models here.
class Photo (models.Model):
    title = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='fallback.png', blank = True)

    def __str__(self):
        return self.title