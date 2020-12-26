from django.shortcuts import render, redirect
from .models import Image, GalleryGroup
from Scripts.grouper import grouper
from random import choice, sample
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from .forms import UserForm, LoginForm, ImageForm, GalleryForm, ChooseGroupForm, EditImageForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

def home_site_view(request):
	images = Image.objects.all().order_by('-date')
	galleries = GalleryGroup.objects.all()

	p = Paginator(images, 5)
	if request.GET.get('page'):
		page_number = request.GET.get('page')
	else:
		page_number = 1
	images_paginator = p.get_page(page_number)

	if len(images) > 0:
		random_image = choice(images)
	else:
		random_image = None
	return render(request, 'home_site/index.html', {'images_paginator':images_paginator, 'random_image': random_image, 'galleries': galleries})

def gallery_view(request, number):
	images = Image.objects.filter(group='group{}'.format(number)).order_by('-date')
	images_template = grouper(images, 3)
	return render(request, 'home_site/index.html', {'images_template':images_template})

def preview_view(request, filename):
	reg = '%{}.%'.format(filename)
	image = Image.objects.extra(where=['image_path LIKE %s'], params=[reg])[0]
	images_count = Image.objects.count()
	if images_count < 4:
		other_images = [Image.objects.filter(pk=index) for index in sample(range(Image.objects.count()), images_count)]
	else:
		other_images = [Image.objects.filter(pk=index) for index in sample(range(Image.objects.count()), 4)]
	if image:
		return render(request, 'home_site/preview.html', {'image': image, 'other_images': other_images})
	else:
		return HttpResponseNotFound('Preview not found!')

def registry_view(request):
	users_count = User.objects.filter(is_superuser=False).count()
	if users_count == 0:
		if request.method == "POST":
			form = UserForm(request.POST)
			if form.is_valid():
				new_user = User.objects.create_user(**form.cleaned_data)
				return redirect("/")
		else:
			form = UserForm()
		return render(request, 'home_site/registry.html', {'form': form})
	else:
		return redirect("/")

def login_view(request):
	users_count = User.objects.filter(is_superuser=False).count()
	if users_count > 0:
		if request.user.is_authenticated:
			return redirect("/menu/")
		if request.method == "POST":
			form = LoginForm(request.POST)
			username = form['username'].value()
			password = form['password'].value()
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("/menu/")
			else:
				form = LoginForm()
				messages.error(request, 'Wrong credentials!')
				return render(request, 'home_site/login.html', {'form': form})
		else:
			form = LoginForm()
			return render(request, 'home_site/login.html', {'form': form})
	else:
		return redirect("/")

def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, "Log out successful!")
		return redirect("/login")
	else:
		return redirect("/")
	

def addimage_view(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = ImageForm(request.POST, request.FILES)
			form.author = request.user
			title = form['title'].value()
			if form.is_valid():
				# to upload enctype="multipart/form-data" needed!
				form.save()
				messages.success(request, 'Image ' + title + ' added!')
			else:
				messages.error(request, 'Image ' + title + ' cannot be added! Check form.')
		form = ImageForm()
		return render(request, 'home_site/add.html', {'form': form})
	else:
		return redirect("/")

def menu_view(request):
	if request.user.is_authenticated:
		return render(request, 'home_site/menu.html')
	else:
		return redirect("/")

def addgallery_view(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = GalleryForm(request.POST)
			title = form['name'].value()
			if form.is_valid():
				form.save()
				messages.success(request, 'Gallery ' + title + ' added!')
			else:
				messages.error(request, 'Gallery ' + title + ' cannot be added! Check form.')
		form = GalleryForm()
		return render(request, 'home_site/addgroup.html', {'form': form})
	else:
		return redirect("/")

def changepassword_view(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = PasswordChangeForm(request.user, request.POST)
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				messages.success(request, 'Password was changed!')
			else:
				messages.error(request, 'Password cannot be changed!')
		form = PasswordChangeForm(request.user)
		return render(request, 'home_site/changepassword.html', {'form': form})
	else:
		return redirect('/')

def editgroup_choice_view(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = ChooseGroupForm(request.POST)
			if form.is_valid():
				group_name = form['gallery_choose'].value()
				return redirect('/menu/editgroup/data/' + str(group_name))
		form = ChooseGroupForm()
		return render(request, 'home_site/groupedit_choice.html', {'form': form})
	else:
		return redirect('/')

def editgroup_data_view(request, groupid):
	if request.user.is_authenticated:
		gallery = GalleryGroup.objects.get(id=groupid)
		if request.method == "POST":
			form = GalleryForm(request.POST, instance=gallery)
			if form.is_valid():
				form.save()
				messages.success(request, 'Group was edited!')
				return redirect('/menu/editgroup/choice')
			else:
				messages.error(request, 'Group cannot be changed!')
		form = GalleryForm(instance=gallery)
		return render(request, 'home_site/groupedit_data.html', {'form': form})
	else:
		return redirect('/')

def editimage_view(request, filename):
	if request.user.is_authenticated:
		reg = '%{}.%'.format(filename)
		image = Image.objects.extra(where=['image_path LIKE %s'], params=[reg])[0]
		if request.method == "POST":
			form = EditImageForm(request.POST, instance=image)
			if form.is_valid():
				form.save()
				return redirect('/preview/' + filename)
			else:
				messages.error(request, 'Image cannot be changed!')
		form = EditImageForm(instance=image)
		return render(request, 'home_site/imageedit.html', {'form': form, 'title': image.title})
	else:
		return redirect('/')

def deleteimage_view(request, filename):
	if request.user.is_authenticated:
		reg = '%{}.%'.format(filename)
		image = Image.objects.extra(where=['image_path LIKE %s'], params=[reg])[0]
		image.delete()
	return redirect('/')
	



