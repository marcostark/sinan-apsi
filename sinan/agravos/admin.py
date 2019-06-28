from django.contrib import admin
from . import models
from .models import (
    Tuberculose, NotificacaoTuberculose,
    NotificaoDengue, Sintomas,
    Doencas, Exames,
    NotificacaoHanseniese,
    Dengue,
)

class SintomasAdmin(admin.ModelAdmin):
    model = models.Sintomas
    list_filter = (
        'nome',
    )

class DoencasAdmin(admin.ModelAdmin):
    model = models.Doencas
    list_filter = (
        'nome',
    )

# TUBERCULOSE ---------------------------------------------------------------------

class NotificacaoTuberculoseInline(admin.StackedInline):
    model = NotificacaoTuberculose
    extra = 1


class TuberculoseAdmin(admin.ModelAdmin):
    model = models.Tuberculose
    inlines = [NotificacaoTuberculoseInline]
    list_display = ['data_notificacao','data_diagnostico','cidade','estado']
    list_filter = (
        'data_notificacao',
        'data_diagnostico',
        'cidade'
    )


class NotificacaoTuberculoseAdmin(admin.ModelAdmin):
    model = models.NotificacaoTuberculose
    list_display = ['inicio_tratamento','unidade_de_saude']
    list_filter = (
        'inicio_tratamento',
        'unidade_de_saude__nome'
    )


# DENGUE ----------------------------------------------------------------------
class ExameInline(admin.TabularInline):
    model = Exames
    extra = 5


class NotificaoDengueInline(admin.StackedInline):
    model = NotificaoDengue
    extra = 1


class NotificacaoDengueAdmin(admin.ModelAdmin):
    model = models.NotificaoDengue
    list_display = ['agravo','sorotipo',]
    list_filter = (
        'sorotipo',
        'agravo',
    )


class DengueAdmin(admin.ModelAdmin):
    model = models.Dengue
    inlines = [NotificaoDengueInline,ExameInline]
    list_display = ['data_notificacao','unidade_de_saude','cidade','data_diagnostico']
    list_filter = (
        'data_notificacao',
        'data_diagnostico',
        'data_primeiros_sintomas',
        'cidade',
    )


# HANSENIESE ---------------------------------------------------------------------

class NotificacaoHansenieseAdmin(admin.ModelAdmin):
    model = models.NotificacaoHanseniese
    list_display = ['agravo','data_diagnostico','grau_incapacidade','inicio_tratamento']
    list_filter = (
        'data_diagnostico',
        'grau_incapacidade',
        'inicio_tratamento',
    )


admin.site.register(Tuberculose, TuberculoseAdmin)
admin.site.register(Dengue, DengueAdmin)
admin.site.register(Sintomas, SintomasAdmin)
admin.site.register(NotificaoDengue, NotificacaoDengueAdmin)
admin.site.register(Doencas, DoencasAdmin)
admin.site.register(NotificacaoTuberculose, NotificacaoTuberculoseAdmin)
admin.site.register(NotificacaoHanseniese, NotificacaoHansenieseAdmin)
#admin.site.register(Exames)
