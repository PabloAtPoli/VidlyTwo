from django.contrib import admin

# Register your models here.
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    
class MovieAdmin(admin.ModelAdmin):
    # exclude = ('date_created', )
    list_display = ('id', 'title', 'number_in_stock', 'daily_rate', 'genre')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

