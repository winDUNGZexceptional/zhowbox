from django.urls import path
from movie import views


app_name = 'movie'

urlpatterns = [
	path('', views.ListPage.as_view(), name='list'),
	path('add/', views.AddPage.as_view(), name='add'),
	# uniformed from movie_id to pk since it will produce error on UpdateView.
	path('movie/<int:pk>/', views.DetailPage.as_view(), name='details'),
	path('movie/<int:pk>/update', views.UpdatePage.as_view(), name='update'),
	path('movie/<int:pk>/delete', views.DeletePage.as_view(), name='delete'),
]