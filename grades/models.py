from django.db import models
from students.models import Student
from courses.models import Course

# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=20)

def __str__(self):
    return f"{self.student} {self.course} {self.grade}"