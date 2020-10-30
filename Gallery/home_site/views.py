from django.shortcuts import render
from .models import Image
from Scripts.grouper import grouper

def home_site_view(request):
	images_amount = Image.objects.count()
	if images_amount < 6:
		image_index = images_amount
	else:
		image_index = 6
	images = Image.objects.order_by('-date')[:image_index]
	images_template = grouper(images, 3)
	return render(request, 'home_site/index.html', {'images_template':images_template})

def gallery_view(request, number):
	images = Image.objects.filter(group='group{}'.format(number)).order_by('-date')
	images_template = grouper(images, 3)
	return render(request, 'home_site/index.html', {'images_template':images_template})
