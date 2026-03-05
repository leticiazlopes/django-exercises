from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return HttpResponse("Welcome to my django blog!")

def eco(request, id):
    return HttpResponse(f"This is the eco page of my blog with ID: {id}")

def info(request):
    return JsonResponse(  {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  })