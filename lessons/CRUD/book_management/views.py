from django.shortcuts import render, redirect
from .models import Book
from .form import ItemForm

def index(req):
    all_books = Book.objects.all()
    return render(req, 'index.html', {'books': all_books})

def create_book(req):
    if req.method == 'POST':
        form = ItemForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    return render(req, 'index.html', {'form': form})