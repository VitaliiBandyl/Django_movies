from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Actor, Genre, Movie, MovieShot, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['name']


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name', 'email']


class MovieShotsInline(admin.TabularInline):
    model = MovieShot
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Shot from Movie"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    list_editable = ['draft']
    search_fields = ('title', 'category__name')
    inlines = [MovieShotsInline, ReviewInline]
    readonly_fields = ['get_image']
    save_on_top = True
    save_as = True
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
        }),
        (None, {
            'fields': (('year', 'world_premier', 'country'),)
        }),
        ("Actors", {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Poster"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['star', 'movie', 'ip']


@admin.register(MovieShot)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ['title', 'movie', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"


admin.site.register(RatingStar)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"
