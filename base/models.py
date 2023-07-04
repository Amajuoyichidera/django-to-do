from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)


    def __str__(self):
        return self.title