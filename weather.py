# Weather
# Going to make a basic weather app that will take in user zip code, and output weather forecast

import requests, json, constants
apikey = constants.TOMORROW_IO_API_KEY
zip = input("Please input your US ZIP code: ")
url = "https://api.tomorrow.io/v4/weather/realtime?apikey=" + apikey + "&location=" + zip + "%20US"


def get_current_weather(zip, url):
    # header options for the http request to tomorrow.io
    headers = {
        "accept-encoding" : "deflat, gzip, br",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response

def print_current_weather(response):
    imported_requests = json.loads(response.text)

    # declare some variables out of the json data. makes thing a little easier when it comes to printing later. 
    req_time = imported_requests["data"]["time"]
    req_location = imported_requests["location"]["name"]
    req_temperature_c = imported_requests["data"]["values"]["temperature"]
    req_temperature_f = ((req_temperature_c*9/5)+32)
    req_precip_prob = imported_requests["data"]["values"]["precipitationProbability"]


    # a little friendly way of telling user if it'll rain. could convert into pictures.
    if req_precip_prob == 100:
        req_willItRain = "It probably is raining right now! Touch grass!"
    elif (req_precip_prob < 100) & (req_precip_prob >= 70):
        req_willItRain = "You should probably grab an umbrella!"
    elif (req_precip_prob < 70) & (req_precip_prob >= 50):
        req_willItRain = "Maybe soon."
    elif (req_precip_prob < 50) & (req_precip_prob >= 30):
        req_willItRain = "Probably not."
    elif (req_precip_prob < 30) & (req_precip_prob > 10):
        req_willItRain = "More than likely not."
    else:
        req_willItRain = "Yeahhhh....No it won't."
    
    # begin the print
    print("Current UTC: " + imported_requests["data"]["time"])
    print("Location: " + imported_requests["location"]["name"])
    print("Temperature: " + str(req_temperature_c) + " °C and " + str(round(req_temperature_f, 2)) + " °F")
    print("Will it rain? " + req_willItRain + " " + str(req_precip_prob) + "% chance")

response = get_current_weather(zip, url)
print_current_weather(response)

# Example JSON response for development reference
# {'data': {'time': 'YYYY-MM-DDTHH:MM:SSZ', 'values': {'altimeterSetting': 1015.46, 'cloudBase': 0.77, 
# 'cloudCeiling': 0.8, 'cloudCover': 55.61, 'dewPoint': 11.2, 'freezingRainIntensity': 0, 'humidity': 67, 
# 'precipitationProbability': 0, 'pressureSeaLevel': 1015.66, 'pressureSurfaceLevel': 1015.13, 'rainIntensity': 0, 
# 'sleetIntensity': 0, 'snowIntensity': 0, 'temperature': 17.57, 'temperatureApparent': 17.6, 'uvHealthConcern': 1, 
# 'uvIndex': 3, 'visibility': 16, 'weatherCode': 1101, 'windDirection': 179, 'windGust': 4.7, 'windSpeed': 2.5}}, 
# 'location': {'lat': NN.NNNNN, 'lon': -NN.NNNNNNN, 'name': 'City, State, Zip, Country', 'type': 'postcode'}}
