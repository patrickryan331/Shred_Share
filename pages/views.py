from django.shortcuts import render
from django.views.generic import TemplateView

from posts.forms import PostCreateForm
from posts.models import Post

import requests
from django.shortcuts import render
from datetime import datetime

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
        
        #  weather url data
        api_key = '271415589d9790f8e8eac3237592a5c0'
        lat, lon = 43.41, 72.72
        cnt = 5

        #ski-resort url data
        app_id = '49acab21'
        app_key = '6ece839b51c0b1e525f77eb12a27c6b7'
        resort_id = 802013

        # https://api.openweathermap.org/data/2.5/weather?lat=43.41&lon=72.72&appid=271415589d9790f8e8eac3237592a5c0&units=imperial

        # https://api/resortforecast/802013?app_id=49acab21&app_key=6ece839b51c0b1e525f77eb12a27c6b7


        # Current weather API call
        current_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial'

        # 5-day forecast API call
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={api_key}&units=imperial'


        # Ski-Resort API call
        ski_resort_url  = f'api/resortforecast/{resort_id}?app_id={app_id}&app_key={app_key}'

        try:
            # Current weather
            current_response = requests.get(current_url)
            current_data = current_response.json()
            
            context['weather'] = {
                'date1': datetime.fromtimestamp(current_data['dt']),
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                'icon': current_data['weather'][0]['icon'],
            }


            # 5-day forecast
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            fiveday_forecast = []
            for item in forecast_data['list']:
                fiveday_forecast.append({
                    'date2': datetime.fromtimestamp(item['dt']),
                    'temp_day': item['temp']['day'],
                    'temp_night': item['temp']['night'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })
            
            context['forecast'] = fiveday_forecast

        except Exception as e:
            context['weather_error'] = str(e)


        

        return context









class StowePageView(MountainDetailsPageView):
    template_name = 'pages/stowe.html'
    mountain_name = "stowe"
    mountain_id = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        api_key = '271415589d9790f8e8eac3237592a5c0'
        lat, lon = 44.52, 72.78
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
                'date1': datetime.fromtimestamp(current_data['dt']),
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                # 'snowcurrent': current_data['snow'],
                'icon': current_data['weather'][0]['icon'],
            }

            # 5-day forecast
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            fiveday_forecast = []
            for item in forecast_data['list']:
                fiveday_forecast.append({
                    'date2': datetime.fromtimestamp(item['dt']),
                    'temp_day': item['temp']['day'],
                    'temp_night': item['temp']['night'],
                    # 'snowforecast': item['snow'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })
            
            context['forecast'] = fiveday_forecast

        except Exception as e:
            context['weather_error'] = str(e)

        return context









class MtSnowPageView(MountainDetailsPageView):
    template_name = 'pages/mtsnow.html'
    mountain_name = "mtsnow"
    mountain_id = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        api_key = '271415589d9790f8e8eac3237592a5c0'
        lat, lon = 42.96, 72.92
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
                'date1': datetime.fromtimestamp(current_data['dt']),
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                # 'snowcurrent': current_data['snow'],
                'icon': current_data['weather'][0]['icon'],
            }

            # 5-day forecast
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            fiveday_forecast = []
            for item in forecast_data['list']:
                fiveday_forecast.append({
                    'date2': datetime.fromtimestamp(item['dt']),
                    'temp_day': item['temp']['day'],
                    'temp_night': item['temp']['night'],
                    # 'snowforecast': item['snow'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })
            
            context['forecast'] = fiveday_forecast

        except Exception as e:
            context['weather_error'] = str(e)

        return context










class KillingtonPageView(MountainDetailsPageView):
    template_name = 'pages/killington.html'
    mountain_name = "killington"
    mountain_id = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        api_key = '271415589d9790f8e8eac3237592a5c0'
        lat, lon = 43.60, 72.82
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
                'date1': datetime.fromtimestamp(current_data['dt']),
                'temperature': current_data['main']['temp'],
                'description': current_data['weather'][0]['description'],
                # 'snowcurrent': current_data['snow'],
                'icon': current_data['weather'][0]['icon'],
            }

            # 5-day forecast
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()
            
            fiveday_forecast = []
            for item in forecast_data['list']:
                fiveday_forecast.append({
                    'date2': datetime.fromtimestamp(item['dt']),
                    'temp_day': item['temp']['day'],
                    'temp_night': item['temp']['night'],
                    # 'snowforecast': item['snow'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })
            
            context['forecast'] = fiveday_forecast

        except Exception as e:
            context['weather_error'] = str(e)

        return context



