from django.urls import path
from accounts.views  import UserSignUp

urlpatterns = [
    path('', UserSignUp.as_view())
]