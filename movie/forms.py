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

	date_screened = forms.DateField(
		widget = forms.widgets.DateInput(format="%m-%d-%Y"),
		input_formats = ("%m-%d-%Y", "%m/%d/%Y"),
		help_text = "MM-DD-YYYY or MM/DD/YYYY"
		)


	class Meta:
		model = Movie
		fields = ['title', 'director', 'summary', 'date_screened',]


