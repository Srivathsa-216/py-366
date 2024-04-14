from django.db import models

# Create your models here.

class Student(models.Model):
    #id = models.AutoField This field will be created automatically from python as primary key
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    address = models.TextField( null = True, blank = True)
    # image = models.ImageField()
    # file = models.FileField()

class Car(models.Model):
    name = models.CharField(max_length = 50)
    top_speed = models.IntegerField(default = 45)

    def __str__(self) -> str:
        return f"MyClass(x={self.name}, y={self.top_speed})"



