from django.db import models

# Create your models here.

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.FloatField()

    def __str__(self):
        return self.nome_produto