from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=128)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Teacher(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
   