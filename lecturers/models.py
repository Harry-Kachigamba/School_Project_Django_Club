from django.db import models

# Create your models here.
class Lecturer(models.Model):
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     subject = models.CharField(max_length=100)

def __str__(self):
     return f"{self.first_name} {self.last_name} {self.subject}"