from django import forms

from movie.models import Movie


# forms.ModelForm instead of forms.Form because we used CreateView, UpdateView, etc.
class AddMovieForm(forms.ModelForm):

	title = forms.CharField(
		max_length = 100, 
		help_text = 'Enter movie title. (Upto 100 characters)'
		)

	director = forms.CharField(
		max_length = 100,
		help_text = 'e.g. John Smith, Joyce Bernal, and/or Juan Dela Cruz'
		)

	# forms.Textarea to convert text field to a <textarea>
	summary = forms.CharField(
		widget = forms.Textarea,
		help_text = 'Please summarize the storyline.'
		)

	# widget to display default format when updating
	date_screened = forms.DateField(
		widget = forms.widgets.DateInput(format="%m-%d-%Y"),
		input_formats = ("%m-%d-%Y", "%m/%d/%Y"),
		help_text = "MM-DD-YYYY or MM/DD/YYYY"
		)


	############# avoid instanciate error on form_class ################ 
	class Meta:
		model = Movie
		fields = ['title', 'director', 'summary', 'date_screened',]



# forms.ModelForm instead of forms.Form because we used CreateView, UpdateView, etc.
class UpdateMovieForm(forms.ModelForm):

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

	# widget to display default format when updating
	date_screened = forms.DateField(
		widget = forms.widgets.DateInput(format="%m-%d-%Y"),
		input_formats = ("%m-%d-%Y", "%m/%d/%Y"),
		help_text = "MM-DD-YYYY or MM/DD/YYYY"
		)

	############# avoid instanciate error on form_class ################ 
	class Meta:
		model = Movie
		fields = ['title', 'director', 'summary', 'date_screened',]
