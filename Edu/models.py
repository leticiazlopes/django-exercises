from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    

class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Livro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=20)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    Editora_id = models.ForeignKey(Editora, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)