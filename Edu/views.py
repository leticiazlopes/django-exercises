from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def livro_list(request):
    livros = Livro.objects.all()
    paginator = Paginator(livros, 10) 
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'Edu/livro_list.html', {'page_obj': page_obj})

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:livro_list')
    else:
        form = LivroForm()
    return render(request, 'Edu/livro_form.html', {'form': form})

def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('edu:livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'Edu/livro_form.html', {'form': form, 'livro': livro})

def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('edu:livro_list')
    return render(request, 'Edu/livro_confirm_delete.html', {'livro': livro})