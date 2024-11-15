from django.urls import path
from .views import UserLoginView, log_user_out, UserSignupView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_user_out, name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]