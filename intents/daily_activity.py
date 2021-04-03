import time
import datetime
from utils.utils import Utils
from utils.speech_recognizes import AgainTakeCommand
import requests


class DailyActivity:
    def __init__(self, logger, response, common_activities, command):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.common_activities = common_activities

    def checking_weather(self):
        print("Inside weather method")
        try:
            api_key = "5957875d5b49b8024c0588be0b4309a6"  # generate your own api key from open weather
            # getting city name from user
            self.response_speak("tell me which city")
            city = AgainTakeCommand.newCommand(self).lower()
            # city = input("Enter city name: ")

            """
            we appending the city valirable and api_key variable to complete the url. for example city name is Mumbai  then url looks like 
            https://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&APPID=4256b3de394a56a86ee35e43af6f5c2e
            """
            data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
            )

            # uncomment the following line and run it so you can get the data in json format
            # print(data.json())

            # getting the data
            print(f"------------ {city} ----------------")
            self.logger.info(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
            self.logger.info(f"Temperature: {data.json().get('main')['temp']}°C")
            self.logger.info(f"Weather: {data.json().get('weather')[0].get('main')}")
            self.logger.info(
                f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C"
            )
            self.logger.info(f"Humidity: {data.json().get('main')['humidity']}%")
            self.logger.info(f"Wind: {data.json().get('wind')['speed']} km/h")

            self.utils.playspeak(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
            self.utils.playspeak(f"Temperature: {data.json().get('main')['temp']}°C")
            self.utils.playspeak(f"Weather: {data.json().get('weather')[0].get('main')}")
            self.utils.playspeak(
                f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C"
            )
            self.utils.playspeak(f"Humidity: {data.json().get('main')['humidity']}%")
            self.utils.playspeak(f"Wind: {data.json().get('wind')['speed']} km/h")
        except Exception as exc:
            print(exc)

    def checking_time(self):
        print("Inside Time method")
        tim = time.strftime('%I:%M %p')
        self.utils.playspeak(f"it's {tim}")

    def checking_date(self):
        print("Inside Date method")
        # This function is for telling the
        # day of the week
        day = datetime.datetime.today().weekday() + 1

        # this line tells us about the number
        # that will help us in telling the day
        day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}

        if day in day_dict.keys():
            day_of_the_week = day_dict[day]
            # print(day_of_the_week)
            self.utils.playspeak("The day is " + day_of_the_week)

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    # get key from voice input
    def get_path_daily(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is', key + " command is " + self.command)
                # Method 2
                #     for activity, path in self.common_activities.items():
                #         print("in for activity is " , activity , "path is : " , path)
                #         if key in activity:
                #             print("if", path)
                #             return path

                for activity in self.common_activities:
                    print("in for activity is ", activity, "path is : ", activity)
                    if key in activity:
                        return self.common_activities[activity]

        except IndexError as e:
            print(e)
        except Exception:
            pass

    def checking_daily_activities(self):
        path = self.get_path_daily()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'weather' or path in 'temperature':
                self.response_speak(self.response)
                self.checking_weather()
            elif path in 'time':
                self.response_speak(self.response)
                self.checking_time()
            elif path in 'day':
                self.response_speak(self.response)
                self.checking_date()

        print(str(path))
