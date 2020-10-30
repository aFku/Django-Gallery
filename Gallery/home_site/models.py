from django.db import models
from django.contrib.auth.models import User
from Scripts.RenamePath import RenamePath
from django.utils import timezone

class Image(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=False)
	user_id = None #przepuscic do funkcji zapisujacej i pobrac z requestu USER ID
	rename_path = RenamePath('Images') # Create object to rename image
	image_path = models.ImageField(upload_to=rename_path, blank=False, default=None) #Size check in form
	title = models.CharField(max_length=100, default='')
	description = models.CharField(max_length=200, default='')
	date = models.DateTimeField(default=timezone.now)
	group = models.CharField(max_length=10, default='group1')


