#!/usr/bin/python3

from twython import Twython
import requests
#import re
from datetime import datetime
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#city = 'newyork'
#res = requests.get('http://wttr.in/{}'.format(city))
#while "Gateway Time-out" in res.text:
#	res = requests.get('http://wttr.in/{}'.format(city))
#raw_data_str = res.text
#raw_data_str = raw_data_str.replace(chr(27),'')
#raw_data_arr = raw_data_str.split('\n')
#data_str = raw_data_arr[2][-13:] + '' + raw_data_arr[3][-49:]
#data_str = re.sub(r'\[.+?m','',data_str)
#while data_str[0].isupper() == False:
#	data_str = data_str[1:]
#data_str = re.sub(r";.*?m.*?\W*",' ',data_str) 
#now = datetime.now()
#current_time = now.strftime("%H:%M")
#extra_data_str = requests.get('http://wttr.in/{}?format=2'.format(city))
#message = current_time + '    ' + data_str + extra_data_str.text[11:]

##############################################################################################################################
import json

response = requests.get('https://api.openweathermap.org/data/2.5/weather?id=5128638&appid=ddd78cdf0cade8ef767c155f8db5cb19&units=imperial')

json_data = response.text
nyc_data  = json.loads(json_data)
now = datetime.now()
current_time = now.strftime("%H:%M")
extra_data_str = requests.get('http://wttr.in/newyork?format=2')

message = current_time + ' ' + nyc_data['weather'][0]['description'].title() + '    ' + 'Temp: ' + str(nyc_data['main']['temp']) + '°F,    ' + \
'Feels Like: ' + str(nyc_data['main']['feels_like']) + '°F,  ' + 'Fluctuations Between: ' + str(nyc_data['main']['temp_min']) + '°F...' + str(nyc_data['main']['temp_max']) +'°F,  ' + \
'Pressure: ' + str(nyc_data['main']['pressure']) + '-inHg,   ' + 'Humidity: ' + str(nyc_data['main']['humidity']) + '%' + '  Wind: ' + extra_data_str.text[11:]

##############################################################################################################################
twitter.update_status(status=message)
print("Tweeted: {}".format(message))

