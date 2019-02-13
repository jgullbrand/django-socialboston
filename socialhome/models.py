from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	#First value is what is stored in the database, second is the displayed value
	TAG_OPTIONS = (
		("Question", "Question"),
		("Event", "Event"),
		("News", "News"),
	)
	title = models.CharField(max_length = 50)
	text = models.TextField()
	tag = models.CharField(max_length = 10, choices = TAG_OPTIONS)
	post_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return f'{self.author:}: {self.title}'

	def get_absolute_url(self):
		return reverse("homepage")		