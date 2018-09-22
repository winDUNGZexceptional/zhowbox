from datetime import date



class SessionHelper:

	@staticmethod
	def get_session(request):
		if request.session.get('last_visited', False):
			last_visited = request.session.get('last_visited')
			SessionHelper.update_session(request)
			return last_visited

		else:
			return 'Welcome to our site!'


	@staticmethod
	def update_session(request):
		request.session['last_visited'] = date.today().strftime("%m-%d-%Y")
		return
