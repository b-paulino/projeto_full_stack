from django.contrib import admin
from cadastro.models import Estudante, Curso, Matricula

class Estudantes(admin.ModelAdmin):
    list_display = ('id','nome','email','cpf','data_nascimento','celular', 'adress',)
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf',)

admin.site.register(Estudante,Estudantes)
class Cursos(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'nivel',)
    list_display_links = ('codigo',)
    list_per_page = 10
    search_fields = ('codigo',)

admin.site.register(Curso,Cursos)

