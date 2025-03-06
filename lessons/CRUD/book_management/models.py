from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = {
        "AC": "Action",
        "RO": "Romance",
        "FI": "Fiction"
    }
    book_title = models.CharField(max_length=30)
    book_author = models.CharField(max_length=50)    
    book_publication_date = models.DateTimeField()
    book_category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='Action')

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name_plural = "Books"