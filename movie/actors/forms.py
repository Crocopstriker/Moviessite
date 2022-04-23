from .models import Maleact
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class MaleactForm(ModelForm):
    class Meta:
        model = Maleact
        fields = ['title', 'best_movies', 'biographi', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "best_movies": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Лучшие фильмы'
            }),
            "biographi": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Биография'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            })
        }
