from django.db import models


class Pais(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
