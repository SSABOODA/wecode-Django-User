from django.urls import path
from accounts.views  import UserSignUp, UserSignin

urlpatterns = [
    path('/signup', UserSignUp.as_view()),
    path('/signin', UserSignin.as_view())
]