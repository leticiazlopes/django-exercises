from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='blog_home'),
    path('eco/<int:id>/', views.eco, name='blog_eco'),
    path('info/', views.info, name='blog_info'),
]
