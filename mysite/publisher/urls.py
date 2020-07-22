from django.urls import path

from .views import PublisherList, PublihserDetail

urlpatterns = [
    path('', PublisherList.as_view(), name='publisher'),
    path('detail/<int:pk>', PublihserDetail.as_view(), name='publisher_detail'),
]
