"""quotes_collector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from quotes_collector import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quotes/', views.quotes_list, name = 'quotes_list_url'),
    path('quote/<int:quote_id>', views.get_specific_quote, name = 'specific_quote_url'),
    path('quote_create', views.create_quote, name = 'create_quote_url'),
    path('authors/', views.authors_list, name='authors_list_url'),
    path('authors_quotes/<int:author_id>', views.get_quotes_by_author, name = 'authors_quotes_url'),
    path('sources/', views.sources_list, name='sources_list_url'),
    path('sources_quotes/<int:source_id>', views.get_quotes_from_source, name = 'sources_quotes_url')
]
