from django import forms
from .models import Book

class ItemForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title', 
                  'book_author', 
                  'book_publication_date', 
                  'book_category',
                  ]