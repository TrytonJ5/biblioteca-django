from django.db import models
from django.contrib.auth.models import User

#model de categoria
class Categoria(models.Model):
    #nome que permite ate no maximo 100 caracteres
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta():
        ordering = ("nome",)

    #auto retorno do nome quando chamado o __str__
    def __str__(self):
        return self.nome
    
#model de Autor
class Autor(models.Model):
    #nome que permite ate no maximo 100 caracteres
    nome = models.CharField(max_length=100, unique= True)

    class Meta():
        ordering = ("nome",)

    #auto retorno do nome quando chamado o __str__
    def __str__(self):
        return self.nome
    
#model de Livro
class Livro(models.Model):
    #titulo que permite ate no maximo 200 caracteres
    titulo = models.CharField(max_length=200, unique=True)
    #relaçao de livro com um autor
    autor = models.ForeignKey(Autor,related_name= "livro", on_delete=models.CASCADE)
    #relaçao de livro com uma categoria
    categoria = models.ForeignKey(Categoria,related_name="livro", on_delete=models.CASCADE)
    #data de publicaçao
    publicado_em = models.DateField()

    class Meta():
        ordering = ("titulo",)

    #auto retorno do nome quando chamado o __str__
    def __str__(self):
        return self.titulo
    
class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Livro, related_name="colecoes")
    colecionador = models.ForeignKey(User, on_delete=models.CASCADE,related_name="colecoes")
    
    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"
 