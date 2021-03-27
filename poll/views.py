from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Teacher, Question, Answer  # using the database

# Home View
def home(request):
 
    questions = Question.objects.all() # grab all the questions
    # render the questions to the home.html template
    return render(request, "home.html", {
        "questions": questions,
    })

# Poll Vote View, receive question_num to know which question we are voting
def poll(request, question_num):

    if request.method == "POST":
        answerId = request.POST["answer"]
        a = Answer.objects.get(id=answerId)
        a.votes += 1
        a.save()
        return HttpResponseRedirect(str(a.question.id) + '/results')
    else:  # GET
        q = Question.objects.get(id=question_num)
        a = list(Answer.objects.filter(question=q))
        return render(request, 'poll_vote.html', {'q': q, 'answers': a})

# Display the results
def results(request, question_num):
    q = Question.objects.get(id=question_num)
    answers = Question.objects.get(id=question_num).answer_set.all()
    return render(request, 'poll_results.html', {'q': q, 'answers': answers})

# Go to the Teacher home page
def teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teacher.html', {'teacher': teacher})

# View for teacher to create a new poll
def teacher_create(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)

    if request.method == "POST":
        q = Question()
        q.question = request.POST["question"]

        q.teacher = teacher
        q.save()

        # This adds all the answers created by teacher to the database
        MAX_ANSWER = 6
        a = [Answer() for _ in range(MAX_ANSWER)]
        for i in range(MAX_ANSWER):
            if "answer" + str(i) in request.POST:
                a[i].answer = request.POST["answer" + str(i)]
                a[i].question = q
                a[i].votes = 0
                a[i].save()
        return render(request, 'teacher.html', {"teacher": teacher})

    return render(request, 'teacher_create.html', {'teacher': teacher})

# View for teacher to delete the poll
def teacher_delete(request, teacher_id):
    question = Question.objects.all()

    if request.method == "POST":

        qid = request.POST['delete']
        q = Question.objects.get(id=qid)

        q.delete()
        teacher = Teacher.objects.get(id=teacher_id)
        return render(request, 'teacher.html', {"teacher": teacher})
    else:
        return render(request, 'teacher_delete.html', {"question": question})
