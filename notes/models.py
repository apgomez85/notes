from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # moment it's added
    updated = models.DateTimeField(auto_now=True)  # moment it's updated
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/entries/{0}/'.format(self.id)

    def get_update_url(self):
        return '/entries/{0}/update/'.format(self.id)
