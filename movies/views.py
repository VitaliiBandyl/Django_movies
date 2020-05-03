from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    """Views for Movies List"""
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "movies/movies.html", context={"movie_list": movie})


class MovieDetailView(View):
    """Detailed movie description"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', context={'movie': movie})