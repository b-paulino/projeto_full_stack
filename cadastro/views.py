from .models import Estudante, Curso, Matricula
from .serializers import CursoSerializer, EstudanteSerializer, MatriculaSerializer
from rest_framework.viewsets import ModelViewSet

class EstudanteViewSet(ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
class CursoViewSet (ModelViewSet):
   queryset = Curso.objects.all()
   serializer_class = CursoSerializer
class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
