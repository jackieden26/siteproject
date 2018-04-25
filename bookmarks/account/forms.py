from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    passowrd = forms.CharField(widget = forms.PasswordInput)
