from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, template_name="movies/index.html", context={"movies": movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, template_name="movies/detail.html", context={"movie": movie})

    # movies = Movie.objects.all()
    # output = ", ".join([m.title for m in movies])
    # return HttpResponse(output)
