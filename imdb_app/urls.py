from django.urls import path
from imdb_app import views

urlpatterns = [
    path('', views.get_movies),
    path('actors/', views.get_actors, name='actors'),
    path('actor-details/<int:id>', views.actor_details, name='actor-details'),
    path('movies/', views.get_movies, name='movies'),
    path('movie-details/<int:id>', views.movie_details, name='movie-details'),
    path('add-movie/', views.add_movie, name='add-movie')
]
