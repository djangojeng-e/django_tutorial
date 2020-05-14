from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Book


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourite_publishers'


class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context





# Create your views here.
