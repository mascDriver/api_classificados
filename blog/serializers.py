from rest_framework import serializers

from .models import Post, Tipo, Imagem


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    imagem = ImagemSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'
