import os

import speech_recognition as sr

from intents.managementsystem import ManagementSystem
from intents.searchanything import SearchAnything
from utils.utils import Utils
from intents.application_list import Application
from intents.daily_activity import DailyActivity
from intents.greeting import Greeting
import threading
import datetime
import sys
import time
import urllib
import subprocess
from playsound import playsound


class Jarvis(threading.Thread):
    def __init__(self, config, logger, os_name):
        threading.Thread.__init__(self)
        self.config = config
        self.logger = logger
        self.os_name = os_name
        self.speech = sr.Recognizer()
        self.utils = Utils(self.logger)

    def checking_system(self):
        playsound('H:\\Pycharm Code\\AI-Assistance-Advanced-Version\\audio\\jarvis_introdation.wav')
        time.sleep(1)

    def check_wifi_status(self):

        # using the check_output() for having the network term retrival
        devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        # decode it to strings
        devices = devices.decode('ascii')
        devices = devices.replace("\r", "")

        # displaying the information
        print(devices)
        self.response_speak("Restarting System, Please Turn on Your Internet Connection First........")
        self.run()

    def read_voice_input(self):
        with sr.Microphone() as source:
            # print("Listening.....")
            self.logger.info("Listening.....")

            try:
                # For reduce noise
                self.speech.adjust_for_ambient_noise(source, duration=0.2)
                audio = self.speech.listen(source, timeout=5, phrase_time_limit=7)
                self.logger.info('Recognizing.....')
                voice_input = self.speech.recognize_google(audio, language='en-in')
                return voice_input.lower()

            except sr.RequestError:
                self.logger.info("Network error...")
            except sr.WaitTimeoutError:
                pass
            except TimeoutError:
                pass
            except Exception:
                pass

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    def takeCommand(self):
        query = self.read_voice_input()
        # query = "hello"
        if query:
            self.logger.info('voice input : {}'.format(query))
            print("user said: " + query)

            return query

    def taskExecution(self):
        while True:
            print("Task Execution Method started Second Loop")
            query = self.takeCommand()
            key = ''
            for key in self.config:
                if query == 'None' or query == 'none':
                    print("Query is none " + query)
                    continue
                else:
                    matched = self.utils.match_utterances(query, self.config[key]['utterances'])
                    if matched:
                        self.logger.info('Executed intent : ' + key)
                        break

                    else:
                        self.logger.info("None.............. say again")
                        # self.read_voice_input()
                        print(key + "  Key and query   ", query)

            if key == 'intent_application':
                apps = self.config[key]['applications']
                # speak here
                response = Utils.choose_random(self.config[key]['response'])
                # self.response_speak(response)

                Application(logger=self.logger, response=response, command=query, applications=apps,
                            os_name=self.os_name).launch()


            elif key == 'intent_sysdata':
                common_system_data = self.config[key]['systemize']
                # speak here
                response = Utils.choose_random(self.config[key]['response'])

                # self.response_speak(response)
                ManagementSystem(logger=self.logger, response=response, command=query,
                                 system_activities=common_system_data, os_name=self.os_name).checking_system_info()

            elif key == 'intent_exit':
                response = Utils.choose_random(self.config[key]['response'])
                self.response_speak(response)
                sys.exit()

            elif key == 'intent_sleep':
                response = Utils.choose_random(self.config[key]['response'])
                self.response_speak(response)
                break

            elif key == 'intent_daily':
                common_data = self.config[key]['common_activities']
                # speak here
                response = Utils.choose_random(self.config[key]['response'])

                # self.response_speak(response)
                DailyActivity(logger=self.logger, response=response, command=query,
                              common_activities=common_data).checking_daily_activities()

            elif key == 'intent_search_google':
                print("query ******************************", query)
                response = Utils.choose_random(self.config[key]['response'])
                self.response_speak(response)
                SearchAnything(logger=self.logger, command=query).searching_on_google()
                print(response)

            elif key == 'intent_None':
                response = Utils.choose_random(self.config[key]['response'])
                # self.response_speak(response)
                self.logger.info(response)
                print(response)
                continue

            else:
                print("In else time part", datetime.datetime.today())

    def run(self):
        host = 'http://google.com'
        if host:
            try:
                urllib.request.urlopen(host)  # Python 3.x
                self.response_speak('checking Internet connection............')
                self.response_speak('Internet Connection is successfully established.....')
                self.welcome()

            except Exception:
                self.response_speak("NO INTERNET CONNECTION detect - jarvis, needs active internet connection")
                self.response_speak("Connect to Internet, there are few network connections i found ")
                self.check_wifi_status()

    def welcome(self):
        self.logger.info('Running thread.........')
        # Checking System First
        # self.checking_system()
        while True:
            print("Main Loop")
            query = self.takeCommand()
            key = ''
            for key in self.config:
                if query == 'None' or query == 'none':
                    print("Query is none " + query)
                    continue
                else:
                    matched = self.utils.match_utterances(query, self.config[key]['utterances'])
                    if matched:
                        self.logger.info('Executed intent : ' + key)
                        break
                    # else:
                    #     self.logger.info("None.............. say again")
                    #     self.read_voice_input()

            if key == 'intent_greeting':
                response = Utils.choose_random(self.config[key]['response'])
                # For Greeting wishing
                Greeting.wish(self)
                self.response_speak(response)
                print(response)
                self.taskExecution()
