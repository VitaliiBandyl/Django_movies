from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    """Views for Movies List"""
    def get(self, request):
        movie = Movie.objects.all()
        return render(request, "movies/movies.html", context={"movie_list": movie})
