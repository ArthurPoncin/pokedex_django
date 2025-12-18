from django.urls import path
from pokedexApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/', views.details, name='details')
]