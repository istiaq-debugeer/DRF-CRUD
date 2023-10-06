from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    City=models.CharField(max_length=30)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.Department