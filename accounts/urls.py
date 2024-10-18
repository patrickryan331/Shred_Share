from django.urls import path
from .views import UserLoginView, log_user_out


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_user_out, name='logout'),
]