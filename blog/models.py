from django.urls import reverse
from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main_menu')
        
class Post(models.Model):  
        
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    textinfo = models.CharField(max_length=250, default='О чем ваш текст?')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_post')
    tags = TaggableManager()
    category = models.CharField(max_length=255, default='N/G')
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '{}/{}'.format(self.title, self.tags)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Написал {} к {}'.format(self.author, self.post)

