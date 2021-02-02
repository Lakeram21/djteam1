from django.db import models

Class Question(models.Model):
    question = models.CharField(max_length=128)