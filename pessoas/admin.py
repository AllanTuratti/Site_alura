from django.contrib import admin
from .models import Pessoa


class Lista_pessoas(admin.ModelAdmin):
    list_display = ("id", "nome_pessoa", "email")
    list_display_links = ("id", "nome_pessoa")
    search_fields = ("nome_pessoa",)
    list_per_page = (2)

admin.site.register(Pessoa, Lista_pessoas)