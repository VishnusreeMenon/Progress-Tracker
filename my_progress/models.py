from re import I
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib import messages
# Create your models here.
class Exercise(models.Model):
    user = models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    exercise_name = models.CharField(max_length=256)
    current_weight = models.IntegerField()
    goal_weight = models.IntegerField()
    rep_count = models.IntegerField()
    
    
    
    def __str__(self):
        return self.exercise_name