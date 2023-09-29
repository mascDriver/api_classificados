from rest_framework import serializers

from .models import Empresa, Contato, Imagem, Prospecto, Categoria


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    contatos = ContatoSerializer(many=True)
    imagens = ImagemSerializer(many=True)

    class Meta:
        model = Empresa
        fields = '__all__'


class ProspectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospecto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    icone = serializers.StringRelatedField()

    class Meta:
        model = Categoria
        fields = '__all__'
