from django.urls import path, include
from .views import index, book

urlpatterns = [
    path('', index, name='books'),

    path('<bookname>', book, name='book'),


]
