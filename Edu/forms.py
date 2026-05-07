from django import forms
from .models import Livro, Editora, Autor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LivroForm(forms.ModelForm):
    Editora_id = forms.ModelChoiceField(queryset=Editora.objects.all(), empty_label="Selecione uma editora", label="Editora")
    autores = forms.ModelMultipleChoiceField(queryset=Autor.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'publicacao', 'preco', 'estoque', 'Editora_id', 'autores']
        widgets = {
            'publicacao': forms.SelectDateWidget,
        }
        
class SignupForm(UserCreationForm):
        email = forms.EmailField(required=True)
        widget = forms.EmailInput(attrs={'placeholder': 'email@exemplo.com', 'class': 'input-text'})

        class Meta:
            model = get_user_model()
            fields = ("username", "email", "password1", "password2")
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este email já está em uso.")
            return email