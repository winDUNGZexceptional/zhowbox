from django.http import JsonResponse



# TO ADD AJAX SUPPORT IN THE LIKE FORM
class AjaxableLike(object):
	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CreateView)
	"""
	def form_invalid(self, form):
		print(form)
		response = super().form_invalid(form)
		print(self)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response

	def form_valid(self, form):
		# We make sure to call the parent's form_valid() method because
		# it might do some processing (in the case of CreateView, it will
		# call form.save() for example).
		response = super().form_valid(form)
		if self.request.is_ajax():
			data = {
			'pk': self.object.pk,
			}
			return JsonResponse(data)
		else:
			return response