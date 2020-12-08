from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Image

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {'password': forms.PasswordInput()}
		labels = {'email': 'Email'}

class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {'password': forms.PasswordInput()}

class ImageForm(ModelForm):
	class Meta:
		model = Image
		fields = ('image_path', 'title', 'description', 'group',)
		exclude = ('author',)
		widgets = {"description": forms.Textarea(attrs={'rows': 5, 'cols':22})}

	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['image_path'].required = False
