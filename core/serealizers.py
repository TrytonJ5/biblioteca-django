from rest_framework import serializers
from core.models import Autor,Categoria,Colecao,Livro

class LivroSerializer(serializers.HyperlinkedModelSerializer):
    autor = serializers.SlugRelatedField(
        queryset = Autor.objects.all(), slug_field="nome"
    )

    categoria = serializers.SlugRelatedField(
        queryset = Categoria.objects.all(), slug_field="nome"
    )

    class Meta():
        model = Livro
        fields = (
            "url",
            "titulo",
            "autor",
            "categoria",
            "publicado_em",
            )

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ("id", "nome")

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "nome")

class ColecaoSerializer(serializers.ModelField):
    livros = serializers.SlugRelatedField(
        queryset =Livro.objects.all(), slug_field="titulo"
    )
    colecionador = serializers.ReadOnlyField(source="colecionador.username")

    class Meta:
        model = Colecao
        fields = ("id","nome","descricao","livros","colecionador")