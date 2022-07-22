from django.urls import path

from . import views

app_name = 'ranking'

urlpatterns = [
    path('', views.ranking, name='home'),
    path('<int:id>', views.modality, name='modality')
]
