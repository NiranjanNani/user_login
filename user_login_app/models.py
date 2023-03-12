from django.db import models

# Create your models here.
class UserDb(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name