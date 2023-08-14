from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Priority(models.Model):
    text = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.text
    
class Todo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text