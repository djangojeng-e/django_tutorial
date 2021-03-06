"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django_tutorial.django_docs.classviewsforms.views import AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('buildingaform.urls')),
    path('contactform/', include('forms_more_on_fields.urls')),
    path('publishers/', include('generic_views.urls')),

    #
    # path('author/add/', AuthorCreate.as_view(), name='author-add'),
    # path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    # path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]
