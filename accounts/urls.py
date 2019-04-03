from .views import SignUp , LoginView , logout_user
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('signup/',SignUp.as_view() , name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout_user/', logout_user ,name='logout_user'),
]