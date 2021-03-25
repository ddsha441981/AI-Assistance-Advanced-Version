from utils.utils import Utils
import datetime
import time


class Greeting:
    def __init__(self, logger, response):
        self.logger = logger
        self.response = response
        self.utils = Utils(self.logger)

    # def speak(self, response):
    #     self.utils.playspeak(response)

    # Day
    def tellDay(self):
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

    # Time
    @staticmethod
    def tellTime(self):
        tim = time.strftime('%I:%M %p')
        self.utils.playspeak(f"it's {tim}")

    # to Wish
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.utils.playspeak('Good Morning Sir.......')
            Greeting.tellTime(self)
            Greeting.tellDay(self)
            # checking_weather()
        elif hour >= 12 and hour < 18:
            self.utils.playspeak('Good Afternoon Sir.......')
            Greeting.tellTime(self)
            Greeting.tellDay(self)
            # checking_weather()
        else:
            self.utils.playspeak('Good Evening.......')
            Greeting.tellTime(self)
            Greeting.tellDay(self)
            # checking_weather(self)
        # self.utils.playspeak('I am Jarvis Sir, Please tell me, how may i help you...')