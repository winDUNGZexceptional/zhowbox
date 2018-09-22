from django.shortcuts import render
from django.views import View

# Create your views here.



class ListPage(View):

	template_name = 'movie/pages/list.html'


	def get(self, request, *args, **kwargs):


		to_render = {

		}
		return render(self.request, self.template_name, to_render)