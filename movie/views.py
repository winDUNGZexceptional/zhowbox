from django import views
from django.urls import reverse_lazy, reverse
from django.views.generic import edit
from django.shortcuts import render

from movie import forms
from movie.models import Movie

# Create your views here.



class ListPage(views.View):

	template_name = 'movie/pages/list.html'


	def get(self, request, *args, **kwargs):

		movie_list = Movie.objects.filter(is_active=True)

		to_render = {
		'movies' : movie_list,
		}
		return render(self.request, self.template_name, to_render)


class DetailPage(views.View):

	template_name = 'movie/pages/details.html'

	def get(self, request, *args, **kwargs):

		movie = Movie.objects.filter(pk=self.kwargs['movie_id']).first()

		to_render = {
		'movie' : movie,
		}
		return render(self.request, self.template_name, to_render)


class AddPage(edit.CreateView):

	model = Movie
	template_name = 'movie/pages/add.html'
	form_class = forms.AddMovieForm

	def get_success_url(self):
		url_param = {
		'movie_id' : self.object.id,
		}
		return reverse('movie:details', kwargs=url_param)

