import requests

class CityWeather:
    city = ""
    api_key = ""

    def __init__(self, city:str, api_key:str):
        self.city = city
        self.api_key = api_key

    def get_temp(self, celcius=True):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

        resp = requests.get(url)
        resp_json = resp.json()

        unprocessed_temp = float(resp_json["main"]["temp"])

        if celcius:
            # converting temperature to celcius
            temp = unprocessed_temp - 273.15

            return float(str(temp)[0:3])

        else:
            return unprocessed_temp

    def is_snow(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

        resp = requests.get(url)
        resp_json = resp.json()

        last_hour_snow = float(resp_json["snow"]["1h"])

        if last_hour_snow < 0.15:
            return False

        else:
            return True

    def get_cloudiness(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

        resp = requests.get(url)
        resp_json = resp.json()

        cloudiness = resp_json["clouds"]["all"]

        return cloudiness

    def get_wind_speed(self, kph=True):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

        resp = requests.get(url)
        resp_json = resp.json()

        unprocessed_wind_speed = float(resp_json["wind"]["speed"])

        if kph:
            # converting m/s to km/h
            wind_speed = unprocessed_wind_speed * 3.6

            return wind_speed

        else:
            return unprocessed_wind_speed

    def get_full_report(self, kph=True, celcius=True):
        wind_speed = self.get_wind_speed(kph)
        cloudiness = self.get_cloudiness()
        snow = self.is_snowfalls()
        temp = self.get_temp(celcius)

        json_data = {
            "temp":temp,
            "snow":snow,
            "cloudiness":cloudiness,
            "wind_speed":wind_speed
        }

        return json_data