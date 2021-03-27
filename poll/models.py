from django.db import models

# teacher model
class Teacher(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)

    def __str__(self):
        return self.firstName

# question model that links to the teacher model
class Question(models.Model):
    question = models.CharField(max_length=128)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

# answer model that links to the question model
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)
    votes = models.IntegerField() 

    def __str__(self):
        return self.answer