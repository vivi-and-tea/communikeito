from django.db import models

from django.db import models
class Word(models.Model):
    kanji = models.CharField(max_length=60)
    hiragana = models.CharField(max_length=60)
    romaji = models.CharField(max_length=60)
    meaning = models.CharField(max_length=60)
    example = models.CharField(max_length=120)
    def __str__(self):
        return self.romaji