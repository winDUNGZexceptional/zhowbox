from django.views.generic import edit
from django.shortcuts import render
from django import views

from movie import forms
from movie.models import Movie

# Create your views here.



class ListPage(views.View):

	template_name = 'movie/pages/list.html'


	def get(self, request, *args, **kwargs):

		to_render = {

		}
		return render(self.request, self.template_name, to_render)



class AddPage(edit.CreateView):

	model = Movie
	template_name = 'movie/pages/add.html'
	form_class = forms.AddMovieForm