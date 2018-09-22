from django.contrib.sessions.backends.db import SessionStore

from datetime import date



class SessionHelper:

	@staticmethod
	def create_session():
		ses = SessionStore()
		ses['last_visited'] = date.today().strftime("%m-%d-%Y")
		ses.save()

		print(ses.session_key)
		return ses.session_key


	@staticmethod
	def get_session(ses_key):
		ses = SessionStore(session_key=ses_key)

		return ses['last_visited']
