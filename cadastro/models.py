from django.db import models

class Estudante(models.Model):
    nome = models.CharField (max_length = 100, null = False, blank = False)
    cpf = models.CharField (max_length = 11, unique = True, null = False, blank = False, primary_key=True)
    email = models.EmailField (unique = True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    endereco = models.CharField(max_length = 255)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    
    def __str__(self):
     return self.nome

class Curso(models.Model):
   nivel = (
      ('B', 'Básico'),
      ('I', 'Intermediário'),
      ('A', 'Avançado'),
   )
   codigo = models.CharField(max_length=14, null=False, blank=False)
   descricao = models.CharField(max_length=500, null=False, blank=False)
   nivel = models.CharField(max_length=1, choices=nivel, blank=False)
   null = False, default = 'B'
   
   def __str__(self):
      return self.codigo
