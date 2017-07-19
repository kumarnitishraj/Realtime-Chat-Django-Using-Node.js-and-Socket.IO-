from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
 
class Comments(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=255)

    def __str__(self):
    	return str(self.user)
