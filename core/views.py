from rest_framework import generics
from core.filters import LivroFilter
from core.models import Autor,Categoria,Livro,Colecao
from core.serealizers import LivroSerializer,AutorSerializer,CategoriaSerializer,ColecaoSerializer
from rest_framework import permissions
from core import custom_permition
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class autorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    name = "autor-list"

class autorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class categoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    name = "categoria-list"

class categoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

class livroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    name = "livro-list"

class livroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

class colecaoList(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-list"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

class colecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-detail"  
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
