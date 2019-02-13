from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from socialboston.storage_backends import MediaStorage
from django.core.files.storage import default_storage as storage


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(storage=MediaStorage(), default="default.jpg", upload_to="profile_pics")

	def __str__(self):
		return f'{self.user.username} profile'

	def save(self, **kwargs):	
		super().save()	

		#img = Image.open(self.image.path)
		img = Image.open(storage.open(self.image.name))
