from django.urls import path
from .views import get_name, index

app_name = 'buildingaform'

urlpatterns = [
    path('', index),
    path('forms/', get_name)
]