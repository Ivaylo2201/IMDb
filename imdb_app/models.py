from django.db import models


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=40)
    photo = models.ImageField(max_length=255)
    summary = models.TextField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Director(Person):
    years_of_experience = models.PositiveIntegerField()


class Actor(Person):
    is_awarded = models.BooleanField(default=False)


class Movie(models.Model):
    title = models.CharField(max_length=25)
    genre = models.CharField(
        choices=[
            ('Sci-Fi', 'Sci-Fi'),
            ('Action', 'Action'),
            ('Comedy', 'Comedy'),
            ('Romance', 'Romance'),
            ('Mystery', 'Mystery'),
            ('Thriller', 'Thriller'),
            ('Fantasy', 'Fantasy'),
        ]
    )
    image = models.URLField(max_length=250)
    script = models.TextField(max_length=200)
    release_date = models.DateField()
    director = models.ForeignKey(
        to=Director,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    protagonist = models.ForeignKey(
        to=Actor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='movies'
    )
    duration = models.PositiveIntegerField()
    trailer = models.CharField()  # The sequence after the '=' in the youtube trailer url

    def __str__(self) -> str:
        return self.title
