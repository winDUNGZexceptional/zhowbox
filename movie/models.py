from django.db import models

# Create your models here.



class Movie(models.Model):

	title = models.CharField(max_length=100, unique=True)
	summary = models.TextField()
	date_screened = models.DateField()
	# director = models.ManyToManyField(Director)
	director = models.CharField(max_length=100)

	likes = models.PositiveIntegerField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)



