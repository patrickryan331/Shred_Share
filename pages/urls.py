from django.urls import path
from pages import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("mountains/", views.MountainPageView.as_view(), name="mountains"),
    path("okemo/", views.OkemoPageView.as_view(), name="okemo"),
    path("stowe/", views.StowePageView.as_view(), name="stowe"),
    path("mtsnow/", views.MtSnowPageView.as_view(), name="mtsnow"),
    path("killington/", views.KillingtonPageView.as_view(), name="killington"),    
    path("meetups/", views.MeetupsPageView.as_view(), name="meetups"),    
]