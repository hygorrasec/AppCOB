from django.urls import path

from . import views

urlpatterns = [
    path('', views.ranking),
    path('<int:id>', views.modality)
]
