from django.shortcuts import render

from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver, editar, crear y borrar Personas.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer