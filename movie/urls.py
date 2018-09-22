from django.urls import path
from movie import views


app_name = 'movie'

urlpatterns = [
	path('', views.ListPage.as_view(), name='list'),
]