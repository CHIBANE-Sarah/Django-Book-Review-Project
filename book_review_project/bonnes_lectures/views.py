from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm

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

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'new_book.html', {'form': form})
