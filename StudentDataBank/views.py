#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Exercise
from django.core import serializers

def index(request):
    return HttpResponse("Welcome to Mobile App Development with BITF20")

def allExercises(request):
    data = serializers.serialize('json', Exercise.objects.all())
    return HttpResponse(data)

def delExercise(request):
    Exercise.objects.filter(pk=int(request.GET['id'])  ).delete()
    return HttpResponse("record of "+request.GET['pk']+" is deleted, if exist already!")

def addExercise(request):
    Exercise(
        exercise_title = request.GET['exercise_title'],
        duration = str(request.GET['duration']),
        reps = int(request.GET['reps']),
        date = str(request.GET['date'])
        ).save()
    return HttpResponse("record of "+request.GET['exercise']+" is added, if does not exist already!")

def updateExercise(request):
    Exercise.objects.filter(pk=int(request.GET['pk'])).update(
        exercise_title = str (request.GET['title']),
        duration = str(request.GET['duration']),
        reps = int(request.GET['reps']),
        date = str(request.GET['date'])
        )
    return HttpResponse("record of "+request.GET['pk']+" is updated, if exist already!")