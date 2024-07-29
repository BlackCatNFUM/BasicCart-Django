from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserChangeFormMod(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width:50%;'}))
    class Meta:
        model = User   
        fields = ('username',)
