from models import *
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'flag_time', 'flag')

class BlacklistForm(ModelForm):
    class Meta:
        model = BlacklistURL
        exclude = ('profile')

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('create_time', 'creator')

class EntryUpdateForm(ModelForm):
    class Meta:
        model = Entry
        exclude = ('create_time', 'creator')

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password' : forms.PasswordInput()
        }
