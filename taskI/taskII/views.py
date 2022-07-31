from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author

# Create your views here.

def index(requist):
    books = Book.objects.all()
    context = {'books':books}
    return render(requist,"taskii/index.html", context)


def book(requist, id):
    book = Book.objects.get(id=id)
    context = {'book':book}
    return render(requist, 'taskii/single_book.html', context)

def author(requist, id):
    author = Author.objects.get(id=id)
    books = author.book_set.all()
    context = {'author': author, 'books': books}
    return render(requist, 'taskii/single_author.html', context)
