from django.shortcuts import render

from rest_framework import viewsets

from .serializers import WordSerializer
from .models import Word

class WordViewset(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('id')
    serializer_class = WordSerializer
