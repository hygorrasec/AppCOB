from django.urls import path

from competicao.views import home

urlpatterns = [
    path('', home),
]
