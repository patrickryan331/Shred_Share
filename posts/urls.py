from django.urls import path
from posts import views

urlpatterns = [
    path("details/<int:pk>/", views.PostDetailView.as_view(), name= 'details')
]