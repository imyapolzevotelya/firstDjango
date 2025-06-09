from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre
from .forms import MovieForm

def movie_list(request):
    genre_filter = request.GET.get('genre')
    if genre_filter:
        movies = Movie.objects.filter(genre__id = genre_filter).order_by('-rating')
    else:
        movies = Movie.objects.all().order_by('-rating')
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres' : genres,
        'selected_genre' : genre_filter
    }
    return render(request, 'movie_detail.html', context)

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movie_detail.html', context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movie_detail.html', context)

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movie_detail.html', context)


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
        context = {
            'form' : form,
            'movie' : movie
        }
    return render(request, 'movie_form.html', context)

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})