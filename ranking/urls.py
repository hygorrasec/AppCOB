from django.urls import path

from . import views

urlpatterns = [
    path('', views.ranking, name='ranking'),
    path('<str:name>', views.modality, name='modality')
]
