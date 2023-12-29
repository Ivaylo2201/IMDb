from django.contrib import admin
from imdb_app.models import Director, Actor, Movie


# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date', 'nationality', 'years_of_experience']
    list_filter = ['nationality', 'years_of_experience']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['birth_date']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date', 'nationality', 'is_awarded']
    list_filter = ['nationality', 'is_awarded']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['birth_date']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date']
    list_filter = ['genre']
    readonly_fields = ['image', 'script', 'release_date', 'duration', 'trailer']
