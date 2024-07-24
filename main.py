import requests
from dotenv import load_dotenv
import os

#loading env
load_dotenv()

TOKEN = os.getenv('TOKEN')
URL ="http://api.weatherapi.com/v1/current.json"

def weather(city, lang='en'):

  """
  This function fetches weather information from given city. Optional param is language.
  """
  
#config
  params = {  'key' : TOKEN,
      'q' : city,
       
      'lang' : lang
    }
    
#Network REquest
  res = requests.get(URL,params)

#Converting to json
  data = res.json()
  #if location not found
  if 'error' in data:
    print('Location not found')
    return
    
# destructuring useful data
  forecast = {
    'temp_c' : data['current']['temp_c'],
    'temp_f' : data['current']['temp_f'],
    'condition' : data['current']['condition']['text'],
    'state' : data['location']['region']
  }
  
  print(forecast)

user_location = input("Enter a location : ")
user_lang = input("Enter lang code defalut(en=English): ")

weather(user_location,user_lang)
