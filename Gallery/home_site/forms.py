from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Image, GalleryGroup

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
		exclude = ['author',]
		widgets = {"description": forms.Textarea(attrs={'rows': 5, 'cols':22})}

	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['image_path'].required = False
		groups = GalleryGroup.objects.all()
		groups_name = [(group.id, group.name) for group in groups]
		self.fields['group'].choices = groups_name

class GalleryForm(ModelForm):
	class Meta:
		model = GalleryGroup
		fields = ('name', 'description')
		widgets = {"description": forms.Textarea(attrs={'rows': 5, 'cols':22})}

class ChooseGroupForm(forms.Form):
	"""
	Groups created in __init__ to allow migrations
	"""
	gallery_choose = forms.ChoiceField(label="Gallery", choices=(), required=True)

	def __init__(self, *args, **kwargs):
		super(ChooseGroupForm, self).__init__(*args, **kwargs)
		self.fields['gallery_choose'].choices = [(group.id, group.name) for group in GalleryGroup.objects.all()]


class EditImageForm(ImageForm):
	def __init__(self, *args, **kwargs):
		ImageForm.__init__(self, *args, **kwargs)
		self.fields.pop('image_path', None)



