from django.shortcuts import render
from django.views.generic import TemplateView

from posts.forms import PostCreateForm
from posts.models import Post

import requests
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class MeetupsPageView(TemplateView):
    template_name = 'pages/meetups.html'


class MountainPageView(TemplateView):
    template_name = 'pages/mountains.html'    


# super class that will handle the form and reading posts
class MountainDetailsPageView(TemplateView):   
    mountain_id = 0 
    mountain_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mountain_id'] = self.mountain_id
        context['mountain_name'] = self.mountain_name
        context["form"] = PostCreateForm()

        # retrieve posts
        posts = Post.objects.filter(mountain_id = self.mountain_id)
        context["posts"] = posts

        return context 



class OkemoPageView(MountainDetailsPageView):
    template_name = 'pages/okemo.html'
    mountain_name = "okemo"
    mountain_id = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        api_key = '271415589d9790f8e8eac3237592a5c0'
        lat, lon = 43.41, 72.72
        cnt = 5

        # Current weather API call
        current_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'

        # 5-day forecast API call
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={api_key}&units=imperial'

        try:
            # Current weather
            current_response = requests.get(current_url)
            current_data = current_response.json()
            
            context['weather'] = {
                'date1': current_data['dt'],
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                # 'percipitation': current_data['percipitation'][0]['mode'],
                # 'type': current_data['percipitation'][0]['value'],
                'icon': current_data['weather'][0]['icon'],
            }

            # 5-day forecast
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            # Process and simplify forecast data
            simplified_forecast = []
            for item in forecast_data['list']:
                simplified_forecast.append({
                    'date2': item['dt'],
                    'temp_day': item['temp']['day'],
                    'temp_night': item['temp']['night'],
                    # 'snow': item['snow'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })
            
            context['forecast'] = simplified_forecast

        except Exception as e:
            context['weather_error'] = str(e)

        return context









class StowePageView(MountainDetailsPageView):
    template_name = 'pages/stowe.html'
    mountain_name = "stowe"
    mountain_id = 2

class MtSnowPageView(MountainDetailsPageView):
    template_name = 'pages/mtsnow.html'
    mountain_name = "mtsnow"
    mountain_id = 3

class KillingtonPageView(MountainDetailsPageView):
    template_name = 'pages/killington.html'
    mountain_name = "killington"
    mountain_id = 4


