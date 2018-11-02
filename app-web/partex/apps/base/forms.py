from django import forms

class ListingCreationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    generic_description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField()

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200)
