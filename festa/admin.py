from django.contrib import admin
from .models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone')

    search_fields = ('nome',)
    list_filter = ('nome',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')
    search_fields = ('nome',)

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro','numero','complemento','bairro','cidade','uf','cep')

    search_fields = ('bairro', 'cidade','logradouro','complemento')
    list_filter = ('bairro','cidade','uf')

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nome','cor_toalha','valor_aluguel')
    list_filter = ('cor_toalha','valor_aluguel')
    search_fields = ('nome',)
    filter_horizontal = ('item',)
    
admin.site.site_header = "Controle de aluguéis"
admin.site.site_title = "Administração das festas"
admin.site.index_title = "Painel de Controle"

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(ItemTema,ItemAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Tema, TemaAdmin)
