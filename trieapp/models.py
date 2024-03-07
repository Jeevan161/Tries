# trieapp/models.py

from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word_text
