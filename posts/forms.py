from django import forms

from .models import *
# class PostForm(forms.Form):
# 	title=forms.Charfield()
# 	discription=forms.Charfield()
# 	image=forms.ImageField()
# 	slug=forms.Charfield()

class PostModelForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','discription','image','slug']