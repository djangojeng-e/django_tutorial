from django.urls import path
from .views import PublisherList

app_name = 'generic_views'

urlpatterns = [

    path('', PublisherList.as_view()),

]
