from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('published', 'published'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='media/post_thumbnail/%Y/%m/%d')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
