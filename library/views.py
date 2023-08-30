from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView,UpdateView, CreateView, DetailView
from library.forms import BookCreateForm
from library.models import Book, Author, Genre

class StartPageView(TemplateView):
    template_name = 'start_page.html'


class ShowBooksView(ListView):
    model = Book
    template_name = 'show_books.html'
    context_object_name = 'books'


class AddBookView(CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('show_books')

    def form_valid(self, form):
        new_author_name = form.cleaned_data['new_author_name']
        new_author_surname = form.cleaned_data['new_author_surname']
        new_genre_name = form.cleaned_data['new_genre_name']

        if new_author_name and new_author_surname:
            author, created = Author.objects.get_or_create(name=new_author_name, surname=new_author_surname)
        else:
            author = None

        if new_genre_name:
            genre, created = Genre.objects.get_or_create(name=new_genre_name)
        else:
            genre = None

        self.object = form.save(commit=False)
        if author:
            self.object.author = author
        self.object.save() 

        if genre:
            self.object.genres.add(genre)  

        return HttpResponseRedirect(self.get_success_url())


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.increase_views()
        return super().get(request, *args, **kwargs)

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'update_book.html'
    form_class = BookCreateForm
    template_name = 'update_book.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('show_books')

    def form_valid(self, form):
        new_author_name = form.cleaned_data['new_author_name']
        new_author_surname = form.cleaned_data['new_author_surname']
        new_genre_name = form.cleaned_data['new_genre_name']

        if new_author_name and new_author_surname:
            author, created = Author.objects.get_or_create(name=new_author_name, surname=new_author_surname)
        else:
            author = None

        if new_genre_name:
            genre, created = Genre.objects.get_or_create(name=new_genre_name)
        else:
            genre = None

        self.object = form.save(commit=False)
        if author:
            self.object.author = author
        self.object.save() 

        if genre:
            self.object.genres.add(genre)  

        return HttpResponseRedirect(self.get_success_url())
    

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('show_books')