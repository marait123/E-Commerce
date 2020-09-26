from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}))
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'content'}))

class LoginForm(forms.Form):

    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))


class RegisterForm(forms.Form):

    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}), required=False)
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}), required=False)
    
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if len(users) > 0:
            raise forms.ValidationError('username already exists')
        return username
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        confirmPassword = data.get('password2')
        if password != confirmPassword:
            raise forms.ValidationError("password must match")
        return data