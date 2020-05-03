from django.db import models
from datetime import date
from django.shortcuts import reverse

class Category(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    """Actors and directors"""
    name = models.CharField("Actor", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"


class Genre(models.Model):
    """Genres"""
    name = models.CharField("Genre", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    """Movies"""
    title = models.CharField("Title", max_length=100)
    tagline = models.CharField("Tagline", max_length=100)
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date", default=2020)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premier = models.DateField("World premier", default=date.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="amount in dollars")
    fees_in_usa = models.PositiveIntegerField("Fees in USA", default=0, help_text="amount in dollars")
    fees_in_world = models.PositiveIntegerField("Fees in world", default=0, help_text="amount in dollars")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("draft", default=False)

    def get_absolute_url(self):
        return reverse('movie_detail_url', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShot(models.Model):
    """Frames from the movie"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Frame from the movie"
        verbose_name_plural = "Frames from the movie"


class RatingStar(models.Model):
    """Rating stars"""
    value = models.SmallIntegerField("Star", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating Star"
        verbose_name_plural = "Rating Stars"


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="Rating Star", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    """Reviews"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Parent", on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
