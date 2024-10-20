from django.db import models

from users.models import User

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.title
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    todo_list = models.ForeignKey(ToDoList, models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.end_date if self.end_date else 'whenever'}"
