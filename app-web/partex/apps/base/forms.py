from django import forms

class ListingCreationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField()

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=200)
    last_name = forms.CharField(label='Last name', max_length=200)
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200)
    email = forms.EmailField(label='Email')
