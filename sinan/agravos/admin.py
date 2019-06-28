from django.contrib import admin
from . import models
from .models import (
    Tipo_Agravo, Notificacao,
    NotificaoDengue, Sintomas,
    Doencas, Exames,
    NotificacaoHanseniese
)


class ExameDengueInline(admin.TabularInline): # TabularInline economiza espaço
    model = Exames


class NotificacaoAdmin(admin.ModelAdmin):
    #inlines = [ExameDengueInline]
    list_display = ['tipo_agravo','inicio_tratamento','unidade_de_saude']
    list_filter = (
        'tipo_agravo',
        'inicio_tratamento',
        'unidade_de_saude'
    )



admin.site.register(Exames)
admin.site.register(Tipo_Agravo)
admin.site.register(Sintomas)
admin.site.register(NotificaoDengue)
admin.site.register(Doencas)
admin.site.register(Notificacao, NotificacaoAdmin)
admin.site.register(NotificacaoHanseniese)

