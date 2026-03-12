from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='blog_home'),
    path('eco/<int:id>/', views.eco, name='blog_eco'),
    path('info/', views.info, name='blog_info'),
    path('index/', views.index, name='blog_index'),
    path('contact/<str:phone>/', views.contact, name='blog_contact'),
    path('about/', views.about, name='blog_about'),
    
]
