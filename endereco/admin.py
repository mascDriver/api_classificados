from django.contrib import admin

from .models import Pais, Estado, Cidade


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    list_filter = ('nome', 'sigla')
    search_fields = ('nome',)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'pais')
    list_filter = ('nome', 'sigla')
    search_fields = ('nome',)
    autocomplete_fields = ('pais',)


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    list_filter = ('estado',)
    search_fields = ('nome',)
    autocomplete_fields = ('estado',)
