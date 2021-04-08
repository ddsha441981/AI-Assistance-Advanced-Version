__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import datetime
import subprocess
import sys
import threading
import time
import urllib

import speech_recognition as sr
from playsound import playsound

from intents.application_list import Application
from intents.automateanything import AutomateAnyThing
from intents.daily_activity import DailyActivity
from intents.greeting import Greeting
from intents.managementsystem import ManagementSystem
from intents.openanything import OpenAnyThing
from intents.searchanything import SearchAnything
from intents.whatsappmsg import WhatsappMessage
from utils.utils import Utils


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
        # self.run()

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
                online_data = self.config[key]['online_content']
                print("query ******************************", query)
                response = Utils.choose_random(self.config[key]['response'])
                # self.response_speak(response)
                SearchAnything(logger=self.logger, response=response, command=query,
                               online_content=online_data).searching_online_content()
                print(response)

            elif key == 'intent_whatsapp':
                print("query ******************************", query)
                response = Utils.choose_random(self.config[key]['response'])
                self.response_speak(response)
                WhatsappMessage(logger=self.logger, command=query, response=response).opening_whatsapp_msg()
                print(response)

            elif key == 'intent_open_websites':
                online_web_data = self.config[key]['web_contents']
                print("query ******************************", query)
                response = Utils.choose_random(self.config[key]['response'])
                print(response)
                OpenAnyThing(logger=self.logger, response=response, command=query,
                               web_contents=online_web_data).opening_anything_web()
                print(response)

            elif key == 'intent_automate_tool':
                automate_data = self.config[key]['automate_tool']
                print("query ******************************", query)
                response = Utils.choose_random(self.config[key]['response'])
                AutomateAnyThing(logger=self.logger, response=response, command=query,
                               automate_tool=automate_data).opening_automate_data()
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
                # self.response_speak("NO INTERNET CONNECTION detect - jarvis, needs active internet connection")
                # self.response_speak("Connect to Internet, there are few network connections i found ")
                # self.check_wifi_status()
                pass

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
