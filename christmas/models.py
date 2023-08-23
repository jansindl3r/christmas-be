from django.db import models
import uuid
# Create your models here.

class Group(models.Model):
    name = models.fields.CharField(max_length=64)
    password = models.fields.CharField(max_length=128)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)

class User(models.Model):
    name = models.fields.CharField(max_length=64)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="users", default="", null=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)

class Wish(models.Model):
    name = models.fields.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishes")
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = "Wishes"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, related_name="comments")
    content = models.fields.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)