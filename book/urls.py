from django.urls import path
from .views import book_list, book_detail, add_book, delete_book, edit_book, add_comment_view, programm_lang_search


urlpatterns = [
    path('books/add_book/', add_book, name='add_book'),
    path('books/delete_book/', delete_book, name='delete_book'),
    path('books/edit_book/', edit_book, name='edit_book'),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('add_comment/', add_comment_view, name='add_comment_view'),
    path('programm_lang_search/', programm_lang_search, name='programm_lang_search'),

]

