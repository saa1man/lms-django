from django.shortcuts import render
from .models import *
from .forms import BookForm

# Create your views here.

def index(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form' : BookForm(),
    }
    return render(request, 'pages/index.html', context=context)

def books(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context=context)