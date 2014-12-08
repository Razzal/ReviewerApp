from django.contrib.auth.models import User
from movie_reviewer.models import ReviewUser
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from datetime import date

class Account():
    def create_account(self, new_username, new_email, new_password):
        new_user = ReviewUser()
        user = User.objects.create_user(username=new_username,password=new_password)
        user.save()
        new_user.user_name = new_username
        new_user.email = new_email
        new_user.user = user
        new_user.user_since = date.today()
        new_user.save()

    def login(self, inc_username, inc_password,request):
        user = authenticate(username=inc_username, password = inc_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return user
            else:
                return 'Account no longer active'
        else:

            return 'Password mismatch'

    def logout(self, request):
        logout(request)

    def validate_new_user(self, username,email, password, passverify):
        if password == passverify:
            print("pass verified")
            namecheck = ReviewUser.objects.filter(user_name=username)
            emailcheck = ReviewUser.objects.filter(email = email)

            print(namecheck)
            print(emailcheck)
            if namecheck:
                return "User Exists"
            if emailcheck:
                return "Email already in use"
            return "True"
        else:
            return "Passwords do not match"


#Make a change password function
