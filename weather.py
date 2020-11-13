import requests
from flask import Flask, request, jsonify, redirect
import os
def get_current_weather(zipcode):
    WEATHER_KEY = os.environ["c"]
    try:
        zipcode=thedict['zipcode']
        countrycode="US"
        wr = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={0},{1}&appid={2}'.format(zipcode,countrycode,WEATHER_KEY))
        weatherdict=wr.json()
    except Exception:
        return dict()
    return weatherdict

