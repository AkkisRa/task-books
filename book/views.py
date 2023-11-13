from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from . import forms
from .forms import AddBookForm, DeleteBookForm, EditBookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Получение данных из формы
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cost = form.cleaned_data['cost']
            created_date = form.cleaned_data['created_date']
            image = form.cleaned_data['image']

            # Создание и сохранение объекта Book
            book = Book.objects.create(
                title=title,
                description=description,
                cost=cost,
                created_date=created_date,
                image=image
            )

            return redirect('book_detail', book_id=book.id)
    else:
        form = AddBookForm()

    return render(request, 'add_book.html', {'form': form})

def delete_book(request):
    if request.method == 'POST':
        form = DeleteBookForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['book_id']
            book = get_object_or_404(Book, title=book_title)
            book.delete()
            return redirect('book_list')
    else:
        form = DeleteBookForm()

    return render(request, 'delete_book.html', {'form': form})


def edit_book(request):
    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                book_id = int(form.cleaned_data['book_id'])

                book = Book.objects.get(pk=book_id)
                book.title = form.cleaned_data['new_title']
                book.description = form.cleaned_data['new_description']
                book.cost = form.cleaned_data['new_cost']
                book.created_date = form.cleaned_data['new_created_date']
                book.image = form.cleaned_data['new_image']

                book.save()

                return redirect('book_detail', book_id=book_id)

            except ValueError:
                pass
    else:
        form = EditBookForm()

    return render(request, 'edit_book.html', {'form': form})
def add_comment_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Коммент успешно добавлен</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'add_comment.html', {'form': form})


def programm_lang_search(request):
    query = request.GET.get('q')

    if query:
        results = Book.objects.filter(title__icontains=query)
    else:
        results = Book.objects.all()

    print(f"Query: {query}, Results: {results}")

    return render(request, 'search_results.html', {'results': results, 'query': query})
