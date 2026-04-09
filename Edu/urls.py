from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('', views.livro_list, name='livro_list'),
    path('create/', views.livro_create, name='livro_create'),
    path('<int:pk>/update/', views.livro_update, name='livro_update'),
    path('<int:pk>/delete/', views.livro_delete, name='livro_delete'),
]
