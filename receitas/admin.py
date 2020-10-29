from django.contrib import admin
from .models import Receita
from .models import Pessoa


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita','tempo_preparo','publicado')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_editable = ('publicado',)
    list_filter = ('categoria',)
    list_per_page = (5)
admin.site.register(Receita, ListandoReceitas)
