from django.urls import path
from movie import views


app_name = 'movie'

urlpatterns = [
	path('', views.ListPage.as_view(), name='list'),
	path('add/', views.AddPage.as_view(), name='add'),
	path('movie/<int:movie_id>/', views.DetailPage.as_view(), name='details'),
	
]