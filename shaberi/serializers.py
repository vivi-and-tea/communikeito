from rest_framework import serializers
from .models import Word

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'kanji', 'hiragana', 'romaji', 'meaning', 'example')