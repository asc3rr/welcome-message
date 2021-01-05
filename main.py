from weather import CityWeather
from gtts import gTTS
import datetime
import playsound
import json

# getting config
config = json.load(open("config.json"))

now = datetime.datetime.now()

hour_m = now.hour
minute = now.minute

year = now.year
month = now.month
day = now.day

date = f"{day}.{month}.{year}"
hour = f"{hour_m}:{minute}"

weather = CityWeather(config["weather"]["city"], config["weather"]["api_key"])

say_conf = config["what_to_say"]
words_conf = config["data_to_say"]

output = ""

# modifying data_to_say
# time
if say_conf["date"]["date"]:
    date = f"{day}.{month}.{year}"

    output += words_conf["date"].replace(":date:", date) + "\n"

if say_conf["date"]["hour"]:
    hour = f"{hour_m}:{minute}"

    output += words_conf["hour"].replace(":hour:", hour) + "\n"

# weather
if say_conf["weather"]["snow"]:
    if weather.is_snow():
        output += words_conf["weather"]["snow"]["pos"] + "\n"

    else:
        output += words_conf["weather"]["snow"]["neg"] + "\n"

if say_conf["weather"]["temp"]:
    temp = weather.get_temp(config["weather"]["celcius"])

    output += words_conf["weather"]["temp"].replace(":temp:", str(temp)) + "\n"

if say_conf["weather"]["cloudiness"]:
    cloudiness = weather.get_cloudiness()

    output += words_conf["weather"]["cloudiness"].replace(":cloudiness:", str(cloudiness)) + "\n"

if say_conf["weather"]["wind_speed"]:
    wind_speed = weather.get_wind_speed()

    output += words_conf["weather"]["wind_speed"].replace(":wind_speed:", str(wind_speed)) + "\n"

tts = gTTS(output, lang=words_conf["language"])
tts.save(config["dir"] + "audio.mp3")

playsound.playsound(config["dir"] + "audio.mp3")