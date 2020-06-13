from rest_framework import serializers

from .models import FlashCard

class FlashCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('front', 'back', 'flashCard_type')