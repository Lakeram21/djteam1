from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('polls/<int:poll_num>', views.poll)
]