from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from imdb_app.models import Actor, Movie
from .forms import MovieForm


# Create your views here.


def get_actors(request) -> HttpResponse:
    actors = Actor.objects.order_by('first_name')

    return render(
        request=request,
        template_name='actors.html',
        context={
            'actors': actors
        }
    )


def actor_details(request, id: int) -> HttpResponse:
    actor = get_object_or_404(Actor, id=id)
    movies = ', '.join(str(m) for m in actor.movies.all())

    return render(
        request=request,
        template_name='actor-details.html',
        context={
            'actor': actor,
            'movies': movies
        }
    )


def get_movies(request) -> HttpResponse:
    movies = Movie.objects.order_by('id')

    return render(
        request=request,
        template_name='movies.html',
        context={
            'movies': movies
        }
    )


def movie_details(request, id: int) -> HttpResponse:
    movie = get_object_or_404(Movie, id=id)

    return render(
        request=request,
        template_name='movie-details.html',
        context={
            'movie': movie
        }
    )


def add_movie(request) -> HttpResponse | HttpResponseRedirect:
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='movies')
    else:
        form = MovieForm()

    return render(
        request=request,
        template_name='add-movie.html',
        context={
            'form': form
        }
    )
