from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Items

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #za validaciju i izbacivanje errora
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError('Username already exists, please pick another!')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError('This email is already in use')
        return email


class ItemForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ['item_name', 'quantity']
