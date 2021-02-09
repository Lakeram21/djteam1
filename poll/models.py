from django.db import models

class Teacher(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)

    def __str__(self):
        return self.firstName

 

class Question(models.Model):
    question = models.CharField(max_length=128)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)
    votes = models.IntegerField() 