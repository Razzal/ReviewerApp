from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=50, required=True)

class CreateUserForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label="Email", max_length=75)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)