from django.urls import path

from . import views

app_name = 'poll'
urlpatterns = [
    path('', views.home),
    path('polls/', views.index, name='index'),
    path('polls/<int:poll_num>', views.poll, name='poll'),
    path('polls/<int:poll_num>/results', views.results, name='results')
]