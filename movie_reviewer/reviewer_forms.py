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
    movie = forms.ModelChoiceField(queryset= Movie.objects.none(), initial=0)
    movie_rating = forms.ChoiceField(choices=RATING_CHOICES)
    movie_comments = forms.CharField(max_length=500, widget=forms.Textarea)
class AddMovieForm(forms.Form):
    movie = forms.CharField(label='Movie Name', max_length=100)
    release_date = forms.DateField(label='Release Date')
    director_first = forms.CharField(label="Directors first name",max_length=25)
    director_last = forms.CharField(label="Directors last name", max_length=25)
    lead_first = forms.CharField(label='Lead star first', max_length=25)
    lead_last = forms.CharField(label='Lead star last', max_length=25)
    genre = forms.CharField(label='Genre', max_length=25)
    runtime = forms.IntegerField(label='Runtime', min_value=0)
    movie_image = forms.FileField(max_length=25, required=False)
    synopsis = forms.CharField(max_length=500, widget=forms.Textarea)

class AddMovieSearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=50, required=True)

