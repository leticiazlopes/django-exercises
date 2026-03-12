from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

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

def index(request):

    servicos = {"nome": "Desenvolvimento Web",
                "descricao": "Criação de sites e aplicações web personalizadas",
                "preco": 1500.00}, {"nome": "Consultoria em SEO",
                "descricao": "Otimização de sites para mecanismos de busca",
                "preco": 800.00}
    
    contexto = {"name": "Leticia",
                "age": 25,
                "hobbies": ["coding", "traveling", "cooking"],
                "city": "São Paulo",
                "now": date.today(),
                "is_logged_in": True,
                "role": "admin",
                "servicos": servicos
                }
    return render(request, 'index.html', contexto)

def contact(request, phone):
    return HttpResponse(f"Contact us at contato@meublog.com or call {phone}")

def about(request):
    return render(request, 'home.html')