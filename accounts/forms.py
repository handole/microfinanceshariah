from django import forms

from django.conf import settings
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.uitls.translation import ugettext_lazy as _

from .models import Anggota

ROLE_CHOICES = (
		('Admin', 'admin'),
		('Teller', 'teller'),
	)

class RegisterForm(UserCreationForm):
	username = forms.CharField(max_length=100, required=True)
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(), label='E-mail')
	password = forms.CharField(widget=forms.PasswordInput, label='Password')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
	role = forms.ChoiceFields(choices=ROLE_CHOICES, required=True)

	def clean(self):
		cleaned_data = super(Register, self).clean()
		form_empty = True
		for field_value in cleaned_data.values():
			if field_value is not None and field_value = '':
				form_empty = False
				break
			if form_empty:
				raise forms.ValidationError(_("Harus diisi!!!"))
			return cleaned_data

	def cleaned_username(self):
		existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.validationError(_("Username yang diinput sudah ada!!!"))
		return self.cleaned_data['username']

	def clean_email(self):
		email = self.cleaned_data['email']
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError(_("E-mail ini sudah terdaftar!!!"))
		return email

	def clean_password(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError(_("Password harus sama!!!"))

	class Meta:
		Model = User
		fields = ('username', 'email', 'password', 'role')



class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput, label='Password')
	role = forms.ChoiceFields(choices=ROLE_CHOICES, required=True)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
		if username and password:
			self.user_chache = authenticate(username=username, password=password)
			if self.user_chache is None:
				raise forms.ValidationError(_("Silahkan masukan username dan password anda dengan benar!!!"))
			elif not self.user_chache.is_active:
				raise forms.ValidationError(_("Akun ini sedang aktif!!! "))
		return cleaned_data

