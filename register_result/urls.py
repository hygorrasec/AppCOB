from django.urls import path

from . import views

urlpatterns = [
    path('', views.register_result, name='register_result'),
]