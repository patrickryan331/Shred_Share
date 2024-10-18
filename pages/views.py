from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'



class MountainPageView(TemplateView):
    template_name = 'pages/mountains.html'


class OkemoPageView(TemplateView):
    template_name = 'pages/okemo.html'

class StowePageView(TemplateView):
    template_name = 'pages/stowe.html'


class MtSnowPageView(TemplateView):
    template_name = 'pages/mtsnow.html'


class KillingtonPageView(TemplateView):
    template_name = 'pages/killington.html'


