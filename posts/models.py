from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Mountain(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="mountains/")
    elevation = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    mountain = models.ForeignKey(Mountain, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(user, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(user, blank=True, null=True, on_delete=models.CASCADE)





