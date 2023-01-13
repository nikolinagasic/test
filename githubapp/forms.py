from django import forms


class UserForm(forms.Form):
    firstName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    bio = forms.CharField(max_length=200)
    company = forms.CharField(max_length=30)
    website = forms.CharField(max_length=100)
    firstName.widget.attrs['class'] = 'edit-profile-input'
    lastName.widget.attrs['class'] = 'edit-profile-input'
    bio.widget.attrs['class'] = 'edit-profile-input'
    company.widget.attrs['class'] = 'edit-profile-input'
    website.widget.attrs['class'] = 'edit-profile-input'
