from django.contrib import admin
from . import models
from .models import (
    Tipo_Agravo, Notificacao,
    NotificaoDengue, Sintomas,
    Doencas, Exames,
    NotificacaoHanseniese, Book
)

class ExameInline(admin.TabularInline):
    model = Exames

class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['tipo_agravo','inicio_tratamento','unidade_de_saude']
    list_filter = (
        'inicio_tratamento',
        'unidade_de_saude__nome'
    )

class NotificacaoDengueAdmin(admin.ModelAdmin):
    inlines = [ExameInline]
    list_display = ['tipo_agravo', 'sorotipo',]
    list_filter = (
        'sorotipo',
        'doencas__nome',
    )


admin.site.register(Tipo_Agravo)
admin.site.register(Sintomas)
admin.site.register(NotificaoDengue, NotificacaoDengueAdmin)
admin.site.register(Doencas)
admin.site.register(Notificacao, NotificacaoAdmin)
admin.site.register(NotificacaoHanseniese)
admin.site.register(Exames)
