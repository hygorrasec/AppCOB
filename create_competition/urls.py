from django.urls import path

from . import views

app_name = 'create_competition'

urlpatterns = [
    path('', views.create_competition, name='home')
]
