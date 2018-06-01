from django.db import models
from user.models import UserProfile
# Create your models here.

class Article(models.Model):
    articleID = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.SET_NULL, null=True, blank=True)
    
    