from django.contrib import admin
from .models import Endereco, Paciente, Unidade_de_Saude, Estado, Cidade



admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Paciente)
admin.site.register(Unidade_de_Saude)