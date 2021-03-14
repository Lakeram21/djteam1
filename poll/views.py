from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Teacher, Question, Answer  # using the database


def home(request):
    # grabbing all the questions
    teachers = Teacher.objects.all()  # getting all the information in questio
    # however i could use an .order_by("type of order") to grab a specifc question.
    questions = Question.objects.all()
    answers = Answer.objects.all()
    return render(request, "home.html", {
        "teachers": teachers,
        "questions": questions,
        "answers": answers})  # attaching the data to the html with a dictionary and we do this using a template context)

    # return render(request, "home.html", {}) # take users to the home.html page


def index(request):
    # grabbing all the questions
    teachers = Teacher.objects.all()  # getting all the information in questio
    # however i could use an .order_by("type of order") to grab a specifc question.
    questions = Question.objects.all()
    answers = Answer.objects.all()
    return render(request, "index.html", {
        "teachers": teachers,
        "questions": questions,
        "answers": answers})  # attaching the data to the html with a dictionary and we do this using a template context)


def poll(request, question_num):
    if request.method == "POST":
        answerId = request.POST["answer"]
        a = Answer.objects.get(id=answerId)
        a.votes += 1
        a.save()
        return HttpResponseRedirect(str(a.question.id) + '/results')
        # return render(request, 'poll_results.html', {'q': Question.objects.get(id=question_num),
        #                                              'a': list(Answer.objects.filter(question=Question.objects.get(id=question_num)))})
    else:  # GET
        q = Question.objects.get(id=question_num)
        a = list(Answer.objects.filter(question=q))
        return render(request, 'poll_vote.html', {'q': q, 'answers': a})


def results(request, question_num):
    q = Question.objects.get(id=question_num)
    # a = list(Answer.objects.filter(question=q))
    answers = Question.objects.get(id=question_num).answer_set.all()
    return render(request, 'poll_results.html', {'q': q, 'answers': answers})

def teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teacher.html', {'teacher': teacher})

def teacher_create(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
 
    if request.method == "POST":
        q = Question()
        q.question = request.POST["question"]
        print(request.POST["question"])
        print("sssssss")
        q.teacher = teacher
        q.save()

        a = [Answer() for _ in range(6)]
        for i in range(6):
            if "answer" + str(i) in request.POST:
                a[i].answer = request.POST["answer" + str(i)]
                a[i].question = q
                a[i].votes = 0
                a[i].save()
        return render(request, 'teacher.html', {"teacher": teacher})

    return render(request, 'teacher_create.html', {'teacher': teacher})



"""
def vote(request):
    vote = request.POST.get('vote')
    vote.votes += 1
    votes.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
"""

