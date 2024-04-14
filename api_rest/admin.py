from django.contrib import admin
from .models import Profissional, Consulta # importando os modelos que criamos em modes

admin.site.register(Profissional)
admin.site.register(Consulta)

