from django.core.validators import MinLengthValidator
from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField


class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Gera automaticamente a URL da empresa, não precisa preencher')
    cnpj = BRCNPJField(unique=True)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    cidade = models.ForeignKey('endereco.Cidade', on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255, validators=[MinLengthValidator(11)])
    bairro = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    cep = BRPostalCodeField()
    numero = models.CharField(max_length=10)
    descricao = models.TextField(null=True, blank=True, help_text='Resumo da empresa sobre o que ela faz')

    def __str__(self):
        return self.nome


class Contato(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='contatos')
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=11)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.empresa.nome


class Imagem(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='imagens')
    banner = models.ImageField(upload_to='imagem_empresas', verbose_name='Banner')
    logo = models.ImageField(upload_to='imagem_empresas', verbose_name='Logo')

    def __str__(self):
        return self.empresa.nome

    class Meta:
        verbose_name_plural = 'Imagens'


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Gera automaticamente a URL da categoria, não precisa preencher')
    icone = models.ForeignKey('CategoriaIcone', on_delete=models.CASCADE,
                              help_text='Para saber qual o icone, acesse: https://mui.com/material-ui/material-icons/')

    def __str__(self):
        return self.nome


class CategoriaIcone(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True,
                            help_text='Para saber qual o icone, acesse: https://mui.com/material-ui/material-icons/')

    def __str__(self):
        return self.nome


class Prospecto(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=11)
    cidade = models.ForeignKey('endereco.Cidade', on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    mensagem = models.TextField(null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
