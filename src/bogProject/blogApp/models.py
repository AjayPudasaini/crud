from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'category_name: {self.name}'

class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'tags_name: {self.name}'


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    article = models.TextField()
    prictue = models.ImageField(upload_to='blogs', default='myPost.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateField(default=timezone.now)


    def __str__(self) -> str:
        return f"{self.author}'s blog post "

