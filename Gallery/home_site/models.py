from django.db import models
from django.contrib.auth.models import User
from Scripts.RenamePath import RenamePath
from django.utils import timezone
from os import remove, path
from django.conf import settings

class Image(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=False, null=True)
	rename_path = RenamePath('Images') # Create object to rename image
	image_path = models.ImageField(upload_to=rename_path, blank=False, default=None, null=True)
	title = models.CharField(max_length=100, default='')
	description = models.CharField(max_length=200, default='')
	date = models.DateTimeField(default=timezone.now)
	group = models.ForeignKey(GalleryGroup, on_delete=models.CASCADE, blank=False, null=False)

	def get_name(self):
		return self.image_path.url.split('/')[-1].split('.')[0]

	def delete(self):
		super().delete()
		print(settings.MEDIA_URL)
		print(settings.MEDIA_ROOT)
		remove(settings.MEDIA_ROOT +  self.image_path.name)

class GalleryGroup(models.Model):
	name = models.CharField(max_length=20, default='')
	description = models.TextField(default='', blank=True)
