from django.db import models
from user.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"commeny by {self.author}, post { self.post}"

    class Meta:
        ordering = ['-comment_date']