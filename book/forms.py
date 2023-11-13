from django import forms
from . import models
from .models import Book

class AddBookForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    cost = forms.DecimalField(label='Цена')
    created_date = forms.DateField(label='Дата выхода', widget=forms.SelectDateWidget)
    image = forms.ImageField(label='Изображение', required=False)


class DeleteBookForm(forms.Form):
    book_id = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label='Выберите книгу для удаления',
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
        to_field_name='title',
    )

    def __init__(self, *args, **kwargs):
        super(DeleteBookForm, self).__init__(*args, **kwargs)
        self.fields['book_id'].queryset = Book.objects.all().values_list('title', flat=True)


class EditBookForm(forms.Form):
    new_title = forms.CharField(label='Новое название', max_length=100)
    new_description = forms.CharField(label='Новое описание', widget=forms.Textarea)
    new_cost = forms.DecimalField(label='Новая цена')
    new_created_date = forms.DateField(label='Новая дата выхода', widget=forms.SelectDateWidget)
    new_image = forms.ImageField(label='Новое изображение', required=False)

    def __init__(self, *args, **kwargs):
        super(EditBookForm, self).__init__(*args, **kwargs)
        self.fields['book_id'] = forms.ChoiceField(
            choices=[(book.id, book.title) for book in Book.objects.all()],
            label='Выберите книгу для редактирования'
        )


class ReviewForm(forms.ModelForm):
    title_lang = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        label='Book',
    )

    class Meta:
        model = models.ReviewProgLang
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title_lang'].queryset = Book.objects.all()
        self.fields['title_lang'].widget.attrs.update({'class': 'form-control'})
