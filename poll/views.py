
'''
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")'''

from django.shortcuts import render
from .models import Teacher, Question # using the database


# Create your views here.
def page(request):
    #grabbing all the questions
    teacher = Teacher.objects.all() #getting all the information in questio
    #however i could use an .order_by("type of order") to grab a specifc question.
    question =Question.objects.all()
    return render(request,"index.html", {"teachDict":teacher, "quest":question}) # attaching the data to the html with a dictionary and we do this using a template context)

