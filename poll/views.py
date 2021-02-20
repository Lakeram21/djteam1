from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Teacher, Question, Answer # using the database

def home(request):
    return render(request, "home.html")

def index(request):
    #grabbing all the questions
    teachers = Teacher.objects.all() #getting all the information in questio
    #however i could use an .order_by("type of order") to grab a specifc question.
    questions = Question.objects.all()
    answers = Answer.objects.all()
    return render(request, "index.html", {
        "teachers": teachers,
        "questions": questions,
        "answers": answers}) # attaching the data to the html with a dictionary and we do this using a template context)

def poll(request, question_num):
    if request.method == "POST":
        # Process POST by incrementing the votes in the corresponding answer by 1 and redirect to the results page
        pass
    else: # GET
        q = Question.object.get(question_num=question_num)
        a = list(Answer.object.filter(question=q))
        return render(request, 'poll_detail.html', {'q': q, 'answers': a})

def results(request, question_num):
    q = Question.object.get(question_num=question_num)
    a = list(Answer.object.filter(question=q))
    return render(request, 'poll_results.html', {'q': q, 'answers': a})

"""
def vote(request):
    vote = request.POST.get('vote')
    vote.votes += 1
    votes.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
"""
