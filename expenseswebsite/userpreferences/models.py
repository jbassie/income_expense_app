from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPreference(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE)
    currency= models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return str(user)+'s' +"preferences"
    