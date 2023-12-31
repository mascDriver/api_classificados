# Generated by Django 4.2.5 on 2023-09-28 13:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0002_auto_20230908_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Gera automaticamente a URL da categoria, não precisa preencher', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaIcone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Para saber qual o icone, acesse: https://mui.com/material-ui/material-icons/', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Gera automaticamente a URL da empresa, não precisa preencher', max_length=255, unique=True)),
                ('cnpj', localflavor.br.models.BRCNPJField(max_length=18, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)])),
                ('endereco', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(11)])),
                ('bairro', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(3)])),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9)),
                ('numero', models.CharField(max_length=10)),
                ('descricao', models.TextField(blank=True, help_text='Resumo da empresa sobre o que ela faz', null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classificados.categoria')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Prospecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(max_length=11)),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classificados.categoria')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='endereco.cidade')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classificados.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='imagem_empresas', verbose_name='Banner')),
                ('logo', models.ImageField(upload_to='imagem_empresas', verbose_name='Logo')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='classificados.empresa')),
            ],
            options={
                'verbose_name_plural': 'Imagens',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('telefone', models.CharField(max_length=11)),
                ('principal', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='classificados.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='icone',
            field=models.ForeignKey(help_text='Para saber qual o icone, acesse: https://mui.com/material-ui/material-icons/', on_delete=django.db.models.deletion.CASCADE, to='classificados.categoriaicone'),
        ),
    ]
