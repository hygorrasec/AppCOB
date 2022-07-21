from django.urls import path

from . import views

urlpatterns = [
    path('', views.ranking),
    path('<str:name>', views.modality)
]
