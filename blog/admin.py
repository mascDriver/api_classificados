from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Post, Tipo, Imagem


class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 1


class PostAdminForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    list_filter = ('tipo__nome',)
    list_display = ('titulo', 'tipo')
    search_fields = ('titulo', 'tipo')
    inlines = [ImagemInline]
    form = PostAdminForm


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome', 'slug')
    search_fields = ('nome', 'slug')


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'blog')
    search_fields = ('imagem', 'blog')
