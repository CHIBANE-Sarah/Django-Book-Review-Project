from django.shortcuts import render
from .models import Book

# Create your views here.
def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})