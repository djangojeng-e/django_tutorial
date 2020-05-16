from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Author

# Create your views here.


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')