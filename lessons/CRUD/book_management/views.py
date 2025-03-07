from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
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

    return render(req, 'edit_book.html', {'form': form})

def edit_book(req, pk):
    book = get_object_or_404(Book, pk=pk)
    if req.method == 'POST':
        form = ItemForm(req.POST, instance=book) 
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=book)

    return render(req, 'edit_book.html', {'form': form})

def delete_book(req, pk):
    book = get_object_or_404(Book, pk=pk)
    if req.method == 'POST':
        book.delete()
        return redirect('index')
    return render(req, 'book_confirm_delete.html', {'book': book})

def search_user(req):
    if req.method == 'POST':
        searched = req.POST['search']
        all_books = Book.objects.filter(
        Q(book_author__icontains=searched) | 
        Q(book_title__icontains=searched) | 
        Q(book_publication_date=searched)
        )
        return render(
            req, 
            'users_searched.html', 
            {'searched': searched,
             'books': all_books
             }
            )
    else:
        return render(req, 'users_searched.html', {})