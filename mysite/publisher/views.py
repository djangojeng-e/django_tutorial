from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book

# Create your views here.

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publisher_list'


class PublihserDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context 
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books 
        context['book_list'] = Book.objects.all() 
        return context