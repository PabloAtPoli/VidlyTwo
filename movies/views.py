from django.http import HttpResponse, Http404
from django.shortcuts import render,  get_object_or_404
from .models import Movie, Genre

# Create your views here.


def index(request):
    # Movie.objects.all()
    # SELECT * FROM movies_movie
    # Movie.objects.filter(id=1)
    # SELECT * FROM movies_movie WHERE id = 1
    # Movie.objects.get(id=1)
    # SELECT * FROM movies_movie WHERE id = 1 LIMIT 1
    # Movie.objects.filter(release_year=1984)
    # SELECT * FROM movies_movie WHERE release_year = 1984

    # movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])

    # movie = Movie.objects.get(id=3)

    # inner join between movies and genre using ORM
    # SELECT * FROM movies_movie INNER JOIN movies_genre ON movies_movie.genre_id = movies_genre.id

    # inner_join = Movie.objects.filter(genre__name='Action')
    # inner_join_output = ""
    # for m in inner_join:
    #     inner_join_output += f'{m.title} - {m.release_year} - {m.genre.name} <br>'

    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    # return HttpResponse(movie_id)
    # try:
    #     movie = Movie.objects.get(pk=movie_id)
    #     return render(request, 'movies/detail.html', {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

