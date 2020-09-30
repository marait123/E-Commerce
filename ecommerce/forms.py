from django import forms
from django.contrib.auth.models import User
formControlClass = "form-control mb-3 d-block"
class ContactForm(forms.Form):
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'first name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'email'}))
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'class':formControlClass,'placeholder':'content'}))

class LoginForm(forms.Form):

    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'username'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':formControlClass,'placeholder':'password'}))


class RegisterForm(forms.Form):

    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'first name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'last name'}), required=False)
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'class':formControlClass,'placeholder':'email'}), required=False)
    
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':formControlClass,'placeholder':'password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':formControlClass,'placeholder':'confirm password'}))
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