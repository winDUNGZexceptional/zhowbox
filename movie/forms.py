from django import forms

from movie.models import Movie


class AddMovieForm(forms.ModelForm):

	title = forms.CharField(
		max_length = 100, 
		help_text = 'Enter movie title. (Upto 100 characters)'
		)

	director = forms.CharField(
		max_length = 100,
		help_text = 'e.g. John Smith, Joyce Bernal, and/or Juan Dela Cruz'
		)

	summary = forms.CharField(
		widget = forms.Textarea,
		help_text = 'Please summarize the storyline.'
		)

	date_screened = forms.DateField()


	class Meta:
		model = Movie
		fields = ['title', 'director', 'summary', 'date_screened',]


