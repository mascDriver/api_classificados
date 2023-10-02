from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Contato, Empresa, Imagem, Categoria, Prospecto, CategoriaIcone


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 1


class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1


class EmpresaAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Empresa
        fields = '__all__'


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome', 'cnpj', 'email', 'telefone', 'cidade', 'endereco', 'bairro', 'cep', 'numero')
    search_fields = ('nome', 'cnpj', 'email', 'cidade')
    list_filter = ('categoria', 'cidade__estado',)
    autocomplete_fields = ('cidade',)
    inlines = [ContatoInline, ImagemInline]
    form = EmpresaAdminForm


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'email', 'telefone', 'principal')
    list_filter = ('empresa', 'email', 'telefone', 'principal')
    search_fields = ('empresa',)
    autocomplete_fields = ('empresa',)


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'banner', 'logo')
    list_filter = ('empresa', 'banner', 'logo')
    search_fields = ('empresa',)
    autocomplete_fields = ('empresa',)


@admin.register(CategoriaIcone)
class CategoriaIconeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome', 'slug')
    search_fields = ('nome',)
    autocomplete_fields = ('icone',)


@admin.register(Prospecto)
class ProspectoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cidade', 'categoria', 'mensagem', 'empresa')
    list_filter = ('categoria', 'cidade')
    search_fields = ('nome', 'email', 'telefone', 'cidade', 'categoria')
    autocomplete_fields = ('cidade', 'categoria', 'empresa')
