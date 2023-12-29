from django.test import TestCase, Client
from django.urls import reverse
from .models import Actor, Movie, Director
from datetime import date

from typing import Final

# Create your tests here.

LOOKUP_FIELDS_ACTORS: Final[list[str]] = [
    'first_name', 'last_name', 'photo'
]

LOOKUP_FIELDS_ACTOR_DETAILS: Final[list[str]] = [
    'first_name', 'last_name', 'birth_date',
    'nationality', 'photo', 'summary', 'is_awarded'
]

LOOKUP_FIELDS_MOVIES: Final[list[str]] = [
    'title', 'image', 'director', 'protagonist'
]

LOOKUP_FIELDS_MOVIE_DETAILS: Final[list[str]] = [
    'title', 'image', 'genre', 'script',
    'release_date', 'director', 'protagonist',
    'duration', 'trailer'
]

class ActorModelTest(TestCase):
    def setUp(self) -> None:
        Actor.objects.create(
            first_name='John',
            last_name='Doe',
            birth_date='1997-01-01',
            nationality='American',
            photo='https://cdn2.momjunction.com/wp-content/uploads/2021/02/What-Is-A-Sigma-Male-And-Their-Common-Personality-Trait-624x702.jpg',
            summary='Test',
            is_awarded=False
        )

    def test_model_attributes(self) -> None:
        actor = Actor.objects.get(first_name='John', last_name='Doe')

        self.assertEqual(actor.first_name, 'John')
        self.assertEqual(actor.last_name, 'Doe')
        self.assertEqual(actor.birth_date, date(1997, 1, 1))
        self.assertEqual(actor.nationality, 'American')
        self.assertEqual(actor.photo, 'https://cdn2.momjunction.com/wp-content/uploads/2021/02/What-Is-A-Sigma-Male-And-Their-Common-Personality-Trait-624x702.jpg'),
        self.assertEqual(actor.summary, 'Test')
        self.assertFalse(actor.is_awarded)

    def test_model_str_representation(self) -> None:
        actor = Actor.objects.get(first_name='John', last_name='Doe')

        self.assertEqual(str(actor), f'{actor.first_name} {actor.last_name}')

class DirectorModelTest(TestCase):
    def setUp(self) -> None:
        self.director = Director.objects.create(
            first_name='John',
            last_name='Smith',
            birth_date='1988-02-02',
            nationality='British',
            photo='https://cdns-images.dzcdn.net/images/artist/086f50bb1ce0e3033634e5e9c2d75462/500x500.jpg',
            summary='Test',
            years_of_experience=15
        )

    def test_model_attributes(self) -> None:
        director = Director.objects.get(first_name='John', last_name='Smith')

        self.assertEqual(director.first_name, 'John')
        self.assertEqual(director.last_name, 'Smith')
        self.assertEqual(director.birth_date, date(1988, 2, 2))
        self.assertEqual(director.nationality, 'British')
        self.assertEqual(director.photo, 'https://cdns-images.dzcdn.net/images/artist/086f50bb1ce0e3033634e5e9c2d75462/500x500.jpg'),
        self.assertEqual(director.summary, 'Test')
        self.assertEqual(director.years_of_experience, 15)

    def test_model_str_representation(self) -> None:
        director = Director.objects.get(first_name='John', last_name='Smith')

        self.assertEqual(str(director), f'{director.first_name} {director.last_name}')

class MovieModelTest(TestCase):
    def setUp(self) -> None:
        Director.objects.create(
            first_name='John',
            last_name='Smith',
            birth_date='1988-02-02',
            nationality='British',
            photo='https://cdns-images.dzcdn.net/images/artist/086f50bb1ce0e3033634e5e9c2d75462/500x500.jpg',
            summary='Test',
            years_of_experience=15
        )

        Actor.objects.create(
            first_name='Jane',
            last_name='Doe',
            birth_date='2000-01-01',
            nationality='Canadian',
            photo='https://static.wikia.nocookie.net/malaverse/images/9/9c/Katherine.jpg/revision/latest/smart/width/250/height/250?cb=20190611110854',
            summary='Test',
            is_awarded=False
        )

        Movie.objects.create(
            title='Testmovie1',
            genre='Comedy',
            image='https://consequence.net/wp-content/uploads/2021/07/rick-astley.jpg',
            script='Test',
            release_date='1969-01-01',
            director=Director.objects.get(first_name='John', last_name='Smith'),
            protagonist=Actor.objects.get(first_name='Jane', last_name='Doe'),
            duration=69,
            trailer='dQw4w9WgXcQ'
        )

    def test_model_attributes(self) -> None:
        movie = Movie.objects.get(title='Testmovie1')
        director = Director.objects.get(first_name='John', last_name='Smith')
        actor = Actor.objects.get(first_name='Jane', last_name='Doe')

        self.assertEqual(movie.title, 'Testmovie1')
        self.assertEqual(movie.genre, 'Comedy')
        self.assertEqual(movie.image, 'https://consequence.net/wp-content/uploads/2021/07/rick-astley.jpg'),
        self.assertEqual(movie.script, 'Test')
        self.assertEqual(movie.release_date, date(1969, 1, 1))
        self.assertEqual(movie.director, director)
        self.assertEqual(movie.protagonist, actor)
        self.assertEqual(movie.duration, 69)
        self.assertEqual(movie.trailer, 'dQw4w9WgXcQ')

    def test_model_str_representation(self) -> None:
        movie = Movie.objects.get(title='Testmovie1')

        self.assertEqual(str(movie), movie.title)

class ActorTestCase(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(
            first_name='John',
            last_name='Doe',
            birth_date='1997-01-01',
            nationality='American',
            photo='https://cdn2.momjunction.com/wp-content/uploads/2021/02/What-Is-A-Sigma-Male-And-Their-Common-Personality-Trait-624x702.jpg',
            summary='Test',
            is_awarded=False
        )

    def test_actors_endpoint(self) -> None:
        client = Client()
        url = reverse('actors')
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        for f in LOOKUP_FIELDS_ACTORS:
            self.assertContains(response, getattr(self.actor, f))

        self.assertTemplateUsed(response, 'actors.html')

    def test_actor_details_endpoint(self) -> None:
        client = Client()
        url = reverse('actor-details', kwargs={'id': 1})
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        for f in LOOKUP_FIELDS_ACTOR_DETAILS:
            if f == 'birth_date':
                self.assertContains(response, 'Jan. 1, 1997')
            elif f == 'is_awarded':
                self.assertContains(response, 'Not awarded yet')
            else:
                self.assertContains(response, getattr(self.actor, f))

        self.assertTemplateUsed(response, 'actor-details.html')


class MovieTestCase(TestCase):
    def setUp(self) -> None:
        self.director = Director.objects.create(
            first_name='John',
            last_name='Smith',
            birth_date='1988-02-02',
            nationality='British',
            photo='https://cdns-images.dzcdn.net/images/artist/086f50bb1ce0e3033634e5e9c2d75462/500x500.jpg',
            summary='Test',
            years_of_experience=15
        )

        self.actor = Actor.objects.create(
            first_name='Jane',
            last_name='Doe',
            birth_date='2000-01-01',
            nationality='Canadian',
            photo='https://static.wikia.nocookie.net/malaverse/images/9/9c/Katherine.jpg/revision/latest/smart/width/250/height/250?cb=20190611110854',
            summary='Test',
            is_awarded=False
        )

        self.movie = Movie.objects.create(
            title='Testmovie1',
            genre='Comedy',
            image='https://consequence.net/wp-content/uploads/2021/07/rick-astley.jpg',
            script='Test',
            release_date='1969-01-01',
            director=self.director,
            protagonist=self.actor,
            duration=69,
            trailer='dQw4w9WgXcQ'
        )

    def test_movies_endpoint(self) -> None:
        client = Client()
        url = reverse('movies')
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        for f in LOOKUP_FIELDS_MOVIES:
            self.assertContains(response, getattr(self.movie, f))

        self.assertTemplateUsed(response, 'movies.html')

    def test_movie_details_endpoint(self) -> None:
        client = Client()
        url = reverse('movie-details', kwargs={'id': 1})
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        for f in LOOKUP_FIELDS_MOVIE_DETAILS:
            if f == 'release_date':
                self.assertContains(response, 'Jan. 1, 1969')
            else:
                self.assertContains(response, getattr(self.movie, f))

        self.assertTemplateUsed(response, 'movie-details.html')

class TestAddMovie(TestCase):
    def test_correct_template(self) -> None:
        client = Client()
        url = reverse('add-movie')
        response = client.get(url)

        self.assertTemplateUsed(response, 'add-movie.html')