from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.user.username