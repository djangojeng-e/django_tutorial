from django.urls import path
from .views import get_name

app_name = 'buildingaform'

urlpatterns = [
    path('forms/', get_name)
]