from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('', views.livro_list, name='livro_list'),
    path('create/', views.livro_create, name='livro_create'),
    path('<int:pk>/update/', views.livro_update, name='livro_update'),
    path('<int:pk>/delete/', views.livro_delete, name='livro_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
]
