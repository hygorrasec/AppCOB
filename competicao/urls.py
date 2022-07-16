from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('modalidade/<str:name>', views.modalidade, name='modalidade')
]
