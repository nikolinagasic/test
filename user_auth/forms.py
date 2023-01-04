from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    bio = forms.CharField(max_length=200)
    company = forms.CharField(max_length=30)
    website = forms.CharField(max_length=30)
