from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200, null=True)
    Text = models.TextField(null=True)
    Author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True, null=True)
    Published_date = models.DateTimeField(null=True)


    def __str__(self):
        return self.name