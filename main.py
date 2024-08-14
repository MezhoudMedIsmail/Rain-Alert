import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")#The api_key is stored as an environment variable to prevent getting your credential used or by someone else.
account_sid = "ACe08d7ee27d92d34c393fc0b37a39y7765"
auth_token = os.environ.get("AUTH_TOKEN") #The token is stored as an environment variable to prevent getting your credential used or stolen by someone else.

weather_params = {
    "lat": "36.817292", # feel free to set your eaxct latitude
    "lon": "10.151342", # feel free to set your eaxct longitude
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"] :
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It will rain today. Don't forget to bring your umbrella !!!",
        from_="XXXXXXXXX", #here your put your twilio number generated from your twilio account
        to="xxxxxxxxx",# here you put your verified number the one u used for verifiying your account
    )
    print(message.status)
