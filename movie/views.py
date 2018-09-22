from django import views
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import edit
from django.shortcuts import render

from movie import forms
from movie.helpers.SessionHelper import SessionHelper
from movie.models import Movie

# Create your views here.



# GET: DISPLAYS ALL THE MOVIES
class ListPage(views.View):

	template_name = 'movie/pages/list.html'

	def get(self, request, *args, **kwargs):
		if 'last_visited' in self.request.session:
			greetings = SessionHelper.get_session(
				self.request.session['last_visited']
				)

			greetings = 'You have visited this page last ' + greetings
		else:
			new_session = SessionHelper.create_session()
			self.request.session['last_visited'] = new_session
			print(self.request.session)
			greetings = 'Welcome to our site!'

		movie_list = Movie.objects.filter(is_active=True)

		to_render = {
		'movies' : movie_list,
		'greetings' : greetings,
		}
		return render(self.request, self.template_name, to_render)


# GET: GET A SINGLE MOVIE AND DISPLAY ALL ITS INFORMATION 
class DetailPage(views.View):

	template_name = 'movie/pages/details.html'

	def get(self, request, *args, **kwargs):
		movie = Movie.objects.filter(pk=self.kwargs['pk']).first()

		to_render = {
		'movie' : movie,
		# 'greetings' : greetings,
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


# GET: (CUSTOM) FORM WILL INITIALLY GO HERE SO TO AVOID CONFIRM TEMPLATE,
# GET(CONT): IT IS REDIRECTED TO THE DELETE METHOD 
# DELETE: (CUSTOM) SOFT DELETION OF THE MOVIE. FROM is_active = True to False
class DeletePage(edit.DeleteView):

	model = Movie

	def get(self, request, *args, **kwargs):
		return self.delete(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		movie = Movie.objects.filter(pk=self.kwargs['pk']).first()
		movie.is_active = False
		movie.save()

		messages.info(self.request, movie.title + " has been deleted.")
		return HttpResponseRedirect( reverse('movie:list') )



# ADD LIKE IN EVERY POST HERE. OF COURSE WITH CSRF FOR SECURITY.
class AddLike(views.View):

	def post(self, request, *args, **kwargs):
		movie = Movie.objects.filter(pk=self.kwargs['pk']).first()
		movie.likes += 1
		movie.save()

		message = {
		'status' : 'success',
		'likes' : movie.likes,
		}
		return JsonResponse(
			message, 
			content_type = 'text/plain; charset=UTF-8',
			safe = False)