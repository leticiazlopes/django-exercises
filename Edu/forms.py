from django import forms
from .models import Livro, Editora, Autor

class LivroForm(forms.ModelForm):
    Editora_id = forms.ModelChoiceField(queryset=Editora.objects.all(), empty_label="Selecione uma editora", label="Editora")
    autores = forms.ModelMultipleChoiceField(queryset=Autor.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'publicacao', 'preco', 'estoque', 'Editora_id', 'autores']
        widgets = {
            'publicacao': forms.SelectDateWidget,
        }