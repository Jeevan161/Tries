"""TrieDictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path 
from . import views
# trieapp/urls.py

urlpatterns = [
     path('', views.trie, name='trie_view'),
   
     path('get_suggestions', views.get_suggestions, name='get_suggestions'),
     path('add_word', views.add_word, name='add_word'),
     path('view_words', views.view_words, name='view_words'),
     path('delete_words', views.delete_words, name='delete_words'),
     path('delete_word/<int:word_id>/', views.delete_word, name='delete_word'),
]
