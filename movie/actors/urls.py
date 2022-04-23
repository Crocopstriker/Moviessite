from django.urls import path
from . import views

urlpatterns = [
    path('', views.actors_home, name='actors_home'),
    path('create', views.create, name='create')
]