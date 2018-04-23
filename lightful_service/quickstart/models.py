from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title=models.TextField(blank=False, default='')
    content=models.TextField(blank=True)
    user_id = models.TextField(blank=False, default=0)
    created_at=models.DateTimeField(blank=True, auto_now_add=True)
    updated_at=models.DateTimeField(blank=True, auto_now_add=True)