from django.shortcuts import render
from django.views.generic import ListView
from .models import Publisher


class PublisherList(ListView):
    model = Publisher




# Create your views here.
