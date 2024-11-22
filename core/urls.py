from django.urls import path
from . import views

urlpatterns = [
     path('autor/',
         views.autorList.as_view(),
         name='autor-list'),
     path('autor/<int:pk>/',
         views.autorDetail.as_view(),
         name='autor-detail'),

     path('categoria/',
         views.categoriaList.as_view(),
         name='categoria-list'),
     path('categoria/<int:pk>/',
         views.categoriaDetail.as_view(),
         name='categoria-detail'),

     path('livros/',
         views.livroList.as_view(), 
         name='livros-list'),
     path('livros/<int:pk>/',
         views.livroDetail.as_view(), 
         name='livro-detail'),

     path('colecao/',
         views.colecaoList.as_view(), 
         name='colecao-list'),
     path('colecao/<int:pk>/',
         views.colecaoDetail.as_view(), 
         name='colecao-detail'),
]
