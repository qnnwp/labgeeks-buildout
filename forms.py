from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(render_value=False))
