import pytest
from django.contrib.auth.models import User
from datetime import date
from .models import Categoria, Autor, Livro, Colecao

@pytest.mark.django_db
def test_categoria_criacao():
    categoria = Categoria.objects.create(nome="Ficção")
    assert categoria.nome == "Ficção"
    assert str(categoria) == "Ficção"

@pytest.mark.django_db
def test_categoria_nome_unico():
    Categoria.objects.create(nome="Aventura")
    with pytest.raises(Exception):
        Categoria.objects.create(nome="Aventura")

@pytest.mark.django_db
def test_autor_criacao():
    autor = Autor.objects.create(nome="J.K. Rowling")
    assert autor.nome == "J.K. Rowling"
    assert str(autor) == "J.K. Rowling"

@pytest.mark.django_db
def test_autor_nome_unico():
    Autor.objects.create(nome="George Orwell")
    with pytest.raises(Exception):
        Autor.objects.create(nome="George Orwell")

@pytest.mark.django_db
def test_livro_criacao():
    categoria = Categoria.objects.create(nome="Fantasia")
    autor = Autor.objects.create(nome="J.R.R. Tolkien")
    livro = Livro.objects.create(
        titulo="O Senhor dos Anéis",
        autor=autor,
        categoria=categoria,
        publicado_em=date(1954, 7, 29),
    )
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == autor
    assert livro.categoria == categoria
    assert livro.publicado_em == date(1954, 7, 29)
    assert str(livro) == "O Senhor dos Anéis"

@pytest.mark.django_db
def test_livro_titulo_unico():
    categoria = Categoria.objects.create(nome="Terror")
    autor = Autor.objects.create(nome="Stephen King")
    Livro.objects.create(
        titulo="It",
        autor=autor,
        categoria=categoria,
        publicado_em=date(1986, 9, 15),
    )
    with pytest.raises(Exception):
        Livro.objects.create(
            titulo="It",
            autor=autor,
            categoria=categoria,
            publicado_em=date(1986, 9, 15),
        )

@pytest.mark.django_db
def test_colecao_criacao():
    usuario = User.objects.create_user(username="colecionador", password="123456")
    categoria = Categoria.objects.create(nome="Clássicos")
    autor = Autor.objects.create(nome="Jane Austen")
    livro = Livro.objects.create(
        titulo="Orgulho e Preconceito",
        autor=autor,
        categoria=categoria,
        publicado_em=date(1813, 1, 28),
    )
    colecao = Colecao.objects.create(
        nome="Favoritos",
        descricao="Meus livros favoritos",
        colecionador=usuario,
    )
    colecao.livros.add(livro)

    assert colecao.nome == "Favoritos"
    assert colecao.descricao == "Meus livros favoritos"
    assert colecao.colecionador == usuario
    assert livro in colecao.livros.all()
    assert str(colecao) == "Favoritos - colecionador"
