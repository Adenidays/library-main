from django import forms
from library.models import Author, Genre, Book


class BookCreateForm(forms.ModelForm):
    new_author_name = forms.CharField(max_length=50, required=False)
    new_author_surname = forms.CharField(max_length=50, required=False)
    new_genre_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genres', 'rating']
