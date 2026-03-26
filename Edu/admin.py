from django.contrib import admin
from .models import Livro, Autor, Editora

# Register your models here.

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo', 'publicacao', 'preco', 'estoque', 'get_editora_nome', 'get_autores_nomes')
    search_fields = ('isbn', 'titulo')
    list_filter = ('publicacao', 'preco', 'estoque')
    filter_horizontal = ('autores',)

    def get_editora_nome(self, obj):
        return obj.Editora_id.nome
    get_editora_nome.short_description = 'Editora'

    def get_autores_nomes(self, obj):
        return ", ".join([autor.nome for autor in obj.autores.all()])
    get_autores_nomes.short_description = 'Autores'