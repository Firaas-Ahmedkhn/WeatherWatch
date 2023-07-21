import time
import pyttsx3 
import requests   

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


city = 'Delhi' #Enter your city here
api_key = '2a4d09d3290b703880ae4903f2e4b956' #Enter your API Key
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


response = requests.get(url)
data = response.json()
weather_desc = data['weather'][0]['description'].capitalize()
temp = data['main']['temp']





timestamp = time.strftime('%H:%M')
print(timestamp)


# speak(f"Today's weather is {weather_desc}")
speak(f"Today's Temprature is {temp}")


if str("6")< timestamp< str("12"):
    speak(f"Good Morning. It's {timestamp} am")
elif str("12") < timestamp < str("20"):
    speak(f"Good Evening. It's {timestamp} pm")
elif str("20") < timestamp < str("24"):
    speak(f"Good Night. It's {timestamp} pm")
elif str("0") < timestamp < str('6'):
    speak(f"Time to sleep. It's {timestamp} am")    


