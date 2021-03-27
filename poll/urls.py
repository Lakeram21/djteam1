from django.urls import path  # for us to use path to route to different views
from . import views           # for us to call different functions in the views.py

app_name = 'poll' # this can help differentiate if there are many different apps in our project
urlpatterns = [
    # home browsing link
    path('', views.home, name="home"), # empty(default) url, calls the home function in the views.py 
    #path('index/', views.index, name='index'),
    # poll views
    path('polls/<int:question_num>', views.poll, name='poll'),
    path('polls/<int:question_num>/results', views.results, name='results'),
    # teacher views
    path('teacher/<int:teacher_id>', views.teacher, name="teacher"),
    path('teacher/<int:teacher_id>/create', views.teacher_create, name="teacher_create"),
    path('teacher/<int:teacher_id>/delete', views.teacher_delete, name="teacher_delete")
]