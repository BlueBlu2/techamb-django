from django.urls import path, include
from .views import index, book, author

urlpatterns = [
    path('', index, name='taski_index'),

    path('books/<int:id>', book, name='single_book'),
    path('authors/<int:id>', author, name='single_author'),


]
