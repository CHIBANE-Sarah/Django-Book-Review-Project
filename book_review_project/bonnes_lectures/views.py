from django.shortcuts import render
from .models import Book

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'book_detail.html', {'book': book})