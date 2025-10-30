from django import forms
from .models import Book
import datetime

class BookForm(forms.ModelForm):
    
    current_year = datetime.date.today().year
    YEAR_CHOICES = [(y, y) for y in range(1900, current_year + 1)][::-1]  # ordre décroissant

    year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'isbn', 'backCover', 'cover']
