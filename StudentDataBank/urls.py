'''
Created on 20-Nov-2023

@author: mianm
'''

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("allExercise", views.allExercises, name="allExercise"),
    path("delExercise", views.delExercise, name="delExercise"),
    path("addExercise", views.addExercise, name="addExercise"),
    path("updateExercise", views.updateExercise, name="updateExercise")
]