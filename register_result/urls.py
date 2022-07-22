from django.urls import path

from . import views

app_name = 'register_result'

urlpatterns = [
    path('', views.register_result, name='home'),
]
