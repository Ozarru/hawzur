from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title

# class Video(models.Model):
#     creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     title = models.CharField(max_length=120, blank=False)
#     snippet = models.CharField(max_length=250, blank=False)
#     description = models.TextField(blank=True, null=True)
#     video = models.FileField(upload_to='videos/')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = 'video'
#         verbose_name_plural = 'videos'
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.title
