from django import views
from django.urls import reverse_lazy, reverse
from django.views.generic import edit
from django.shortcuts import render

from movie import forms
from movie.models import Movie

# Create your views here.



# GET: DISPLAYS ALL THE MOVIES
class ListPage(views.View):

	template_name = 'movie/pages/list.html'


	def get(self, request, *args, **kwargs):

		movie_list = Movie.objects.filter(is_active=True)

		to_render = {
		'movies' : movie_list,
		}
		return render(self.request, self.template_name, to_render)


# GET: GET A SINGLE MOVIE AND DISPLAY ALL ITS INFORMATION 
class DetailPage(views.View):

	template_name = 'movie/pages/details.html'

	def get(self, request, *args, **kwargs):

		movie = Movie.objects.filter(pk=self.kwargs['pk']).first()

		to_render = {
		'movie' : movie,
		}
		return render(self.request, self.template_name, to_render)


# GET: (DEFAULT) DISPLAY THE TEMPLATE FORM ON template_name
# POST: (DEFAULT) CREATE THE OBJECT IF PASSED forms.AddMovieForm
# self.object == object recently created by the form.
# get_success_url TO REDIRECT TO DETAIL PAGE OF RECENTLY CREATED
class AddPage(edit.CreateView):

	model = Movie
	template_name = 'movie/pages/add.html'
	form_class = forms.AddMovieForm

	def get_success_url(self):
		url_param = {
		'pk' : self.object.id,
		}
		return reverse('movie:details', kwargs=url_param)


# GET: (DEFAULT) DISPLAY THE TEMPLATE FORM WITH VALUES
# POST: (DEFAULT) UPDATE/MODIFY THE OBJECT WITH pk IN URLS.PY
# self.object == object recently created by the form.
# get_success_url TO REDIRECT TO DETAIL PAGE OF RECENTLY MODIFIED
class UpdatePage(edit.UpdateView):

	model = Movie
	template_name = 'movie/pages/update.html'
	form_class = forms.UpdateMovieForm

	def get_success_url(self):
		url_param = {
		'pk' : self.object.id,
		}
		return reverse('movie:details', kwargs=url_param)