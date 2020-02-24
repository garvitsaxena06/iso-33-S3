from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class DiseaseRegisterForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	virus =  forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	locality = forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	prec = forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	symp = forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	cause = forms.CharField(widget=forms.TextInput(), required=True, max_length=40)

	class Meta():
		model = diseases
		fields = ['name', 'virus', 'locality', 'prec', 'symp', 'cause']


class feedbackform(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	email=forms.CharField(widget=forms.TextInput(), required=True, max_length=40)
	contactno=forms.CharField(widget=forms.NumberInput(), required=True, max_length=10)
	feed=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

	class Meta():
		model = feedback
		fields = ['name', 'email', 'contactno', 'feed']		