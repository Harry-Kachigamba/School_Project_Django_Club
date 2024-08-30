from django.db import models
from lecturers.models import Lecturer

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

def __str__(self):
    return self.name