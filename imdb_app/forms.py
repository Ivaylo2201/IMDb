from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        )
    )

    class Meta:
        model = Movie
        fields = [
            'title', 'genre', 'image',
            'script', 'release_date', 'director',
            'protagonist', 'duration', 'trailer'
        ]
