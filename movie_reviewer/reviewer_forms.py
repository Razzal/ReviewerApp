from django import forms
from movie_reviewer.models import Movie

RATING_CHOICES = [(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10),]

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
class AddReviewForm(forms.Form):
    movie = forms.ModelChoiceField(queryset= Movie.objects.all(), initial=0)
    movie_rating = forms.ChoiceField(choices=RATING_CHOICES)
    movie_comments = forms.CharField(max_length=5000, widget=forms.Textarea)