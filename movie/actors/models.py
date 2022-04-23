from typing import Tuple

from django.db import models
from django.db.models import CharField


class Maleact(models.Model):
    title = models.CharField('Имя', max_length=100, default="")
    best_movies = models.CharField('Лучшие фильмы', max_length=100, default="")
    biographi = models.TextField('Биография', max_length=250, default="")
    date = models.DateField('Дата рождения')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'




