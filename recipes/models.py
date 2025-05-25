from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    #Foreign key for one to many relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    
    #Model data
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    prep_time = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title