from django.core.management.base import BaseCommand
from Edu.models import Livro, Editora, Autor
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Cria livros de exemplo usando Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        
        editoras = list(Editora.objects.all())
        autores = list(Autor.objects.all())

        if not editoras or not autores:
            self.stdout.write(self.style.ERROR('Erro: Você precisa ter pelo menos uma Editora e um Autor no banco!'))
            return

        for _ in range(100): 
            
            livro = Livro.objects.create(
                isbn=fake.isbn13().replace("-", "")[:13],
                titulo=fake.catch_phrase()[:20], 
                publicacao=fake.date_this_century(),
                preco=round(random.uniform(19.90, 99.90), 2),
                estoque=random.randint(1, 50),
                Editora_id=random.choice(editoras) 
            )
            
            
            livro.autores.add(random.choice(autores))

        self.stdout.write(self.style.SUCCESS(f'Sucesso! Criados 100 livros. Total no banco: {Livro.objects.count()}'))