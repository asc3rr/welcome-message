# welcome message
Text message that is played after logging into system.

## Configuration
```json
{
    "dir":"./", # directory for saving audio files (you must write permission to this directory)
    "weather":{
        "api_key":"", # open weathermap api key
        "city":"", # city to get weather
        "celcius":true,
        "kph":true
    },
    "what_to_say":{
        "weather":{
            "snow":true,
            "temp":true,
            "cloudiness":true,
            "wind_speed":true
        },
        "date":{
            "date":true,
            "hour":true
        }
    },
    "data_to_say":{
        "weather":{
            "snow":{
                "pos":"Możliwe opady śniegu", # when snow is falling
                "neg":"Dzisiaj nie są przewidziane opady śniegu" # when snow if not falling
            },
            "temp":"Dzisiaj mamy :temp:°C", # text for temperature
            "cloudiness":"Zachmurzenie na poziomie :cloudiness:%", # text for cloudiness
            "wind_speed":"Prędkość wiatru: :wind_speed: km/h" # text for wind speed
        },
        "date":"Dzisiaj jest :date:", # text for date
        "hour":"Jest godzina :hour:", # text for hour
        "language":"pl" # language for gTTS
    }
}
```

## Bugs
- [] Special characters not supported
