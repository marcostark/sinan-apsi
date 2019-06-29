from django.contrib import admin
from .models import Endereco, Paciente, Unidade_de_Saude, Estado, Cidade

class EstadoAdmin(admin.ModelAdmin):
    resource_class = Estado
    list_display = ['nome','codigo_ibge',]


class CidadeAdmin(admin.ModelAdmin):
    resource_class = Cidade
    list_display = ['nome','codigo_ibge','estado']
    list_filter = (
        'nome',
    )

class PacienteAdmin(admin.ModelAdmin):
    resource_class = Paciente
    list_display = ['nome_completo','data_nascimento','sexo']
    list_filter = (
        'nome_completo',
    )

class UnidadeSaudeAdmin(admin.ModelAdmin):
    model = Unidade_de_Saude
    list_display = ['id','nome','cidade',]
    list_filter = (
        'cidade',
    )


admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Endereco)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Unidade_de_Saude, UnidadeSaudeAdmin)