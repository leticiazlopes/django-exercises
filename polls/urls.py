from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='polls_hello'),
]
