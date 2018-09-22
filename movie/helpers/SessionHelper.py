from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from datetime import date


def create_session():
	ses = SessionStore()
	update_session(ses)

	print(ses.session_key)
	return ses.session_key


def update_session(ses):
	ses['last_visited'] = date.today().strftime("%m-%d-%Y")
	ses.save()

	print(ses.session_key)
	print('updated')
	return


def get_session(ses_key):
	ses = SessionStore(session_key=ses_key)
	last_visited = ses['last_visited']

	update_session(ses)

	return ses['last_visited']


# CREATE A SESSION AND PASS TO THE FUNCTION 
def session_decorator(view_function):
	def wrapper(request, *args, **kwargs):

		if 'last_visited' not in request.session:
			session_here = create_session()
			request.session['last_visited'] = session_here

			# THIS DEFINE THAT THE SESSION IS NEW
			message = {'message': 'Welcome to our site!'}

		else:
			print(request.session)
			existing_ses = SessionStore(
				session_key=request.session['last_visited']
				)
			update_session(existing_ses)
			
			text = 'Welcome back! Your last visit was from ' + existing_ses['last_visited']
			message	= {'message': text}

		# send the message to the view
		response = view_function(request, *args, kwargs=message)

		# return redirect( reverse(view_function, args=args, kwargs=kwargs) )
		return response

	return wrapper
