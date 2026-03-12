from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo (models.Model):
    title = models.CharField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='fallback.png', blank = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title