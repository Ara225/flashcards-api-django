from django.shortcuts import render

from rest_framework import viewsets

from .serializers import FlashCardSerializer
from .models import FlashCard


class FlashCardViewSet(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all().order_by('front')
    serializer_class = FlashCardSerializer
