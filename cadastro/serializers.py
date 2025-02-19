from rest_framework import serializers
from .models import Estudante, Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudanteSerializer(serializers.ModelSerializer):
    curso_nome = serializers.ReadOnlyField(source = 'curso.nome')
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular', 'adress']