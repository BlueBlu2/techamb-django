from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
book_list=["book1", "book2", "book3"]
book_data=[]
def index(request):
    book_data.clear()
    readf()
    context={'books':book_data}
    print(context)
    return render(request, 'books/books.html',context)


def book(request, bookname):
    bookname = bookname.translate({ord(i):None for i in "[]'"})
    context = {'bookname':bookname.split(",") }
    print(context)
    return render(request, 'books/book.html', context)


def readf():

    with open('static/readme.txt', 'r') as f:
        for line in f:
            book_data.append(line.split())

        print(book_data)

#=f.read().split()