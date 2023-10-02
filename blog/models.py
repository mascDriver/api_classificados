from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.nome


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    conteudo = models.TextField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Imagem(models.Model):
    imagem = models.ImageField(upload_to='blog')
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagem')

    def __str__(self):
        return self.imagem.url

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
