__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import re
import webbrowser
import requests
import whois
from geopy import Nominatim  # For Zip Code

from utils.speech_recognizes import AgainTakeCommand
from utils.utils import Utils


class OpenAnyThing:
    def __init__(self, logger, response, web_contents, command):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.web_contents = web_contents

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    # Open Any Website
    def any_website_opener(self, website_name):
        extension = re.search(r"[.]", website_name)
        if not extension:
            if not website_name.endswith(".com"):
                website_name = website_name + ".com"
        try:
            url = 'https://www.' + website_name
            webbrowser.open(url)
            return True
        except Exception as e:
            print(e)
            return False

    # Checking IFSC Code
    def checking_ifsc_code(self, ifsc_code):
        self.response_speak('Checking ifsc code ............')
        try:
            # Assign IFSC code and URL
            # IFSC_Code = 'SBIN0018666'
            URL = "https://ifsc.razorpay.com/"

            # Use get() method
            data = requests.get(URL + ifsc_code).json()
            print("-----------------Bank IFSC Code-----------------")
            for key, value in data.items():
                print(key, " :- ", value)


        except ConnectionError as er:
            print(er)
        except Exception as err:
            print(err)

    # Checking Zip Code
    def checking_zip_code(self, zipcode):
        try:
            # Using Nominatim Api
            geolocator = Nominatim(user_agent="geoapiExercises")

            # Using geocode()
            location = geolocator.geocode(zipcode)

            # Displaying address details
            print("Zipcode:", zipcode)
            print("Details of the Zipcode:")
            print(location)

        except ConnectionError as er:
            print(er)
        except Exception as err:
            print(err)

    # Checking Domain Name
    def checking_domain_name(self, domain_url):
        self.response_speak("Checking domain name....")
        try:
            domain_info = whois.whois(domain_url)

            for key, value in domain_info.items():
                print(str(key) + " : -  " + str(value))
        except ConnectionError as er:
            print(er)
        except Exception as err:
            print(err)

    # get key from voice input
    def get_path_open_anything(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is', key + " command is " + self.command)

                for web_online in self.web_contents:
                    print("in for activity is ", web_online, "path is : ", web_online)
                    if key in web_online:
                        return self.web_contents[web_online]

        except IndexError as e:
            print(e)
        except Exception:
            pass

    def opening_anything_web(self):
        path = self.get_path_open_anything()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'website':
                self.response_speak("which website do you want open!!")
                website_name = AgainTakeCommand.newCommand(self).lower()
                self.response_speak(self.response)
                self.any_website_opener(website_name)

            elif path in 'zip code' or path in 'pin code' or path in 'pin' or path in 'zip':
                self.response_speak("Please Provide me zipcode...")
                zipcode = int(input("Enter zipcode here!!!!!! \n "))
                self.response_speak(self.response)
                self.checking_zip_code(zipcode)

            elif path in 'ifsc' or path in 'ifsc code':
                self.response_speak("Please provide me ifsc code.....")
                ifsc_code = input("Enter ifsc code here!!!!!! \n")
                self.checking_ifsc_code(ifsc_code)

            elif path in 'domain':
                self.response_speak("Please provide me domain name.....")
                domain_url = input("Enter domain name here!!!!!! \n")
                self.checking_domain_name(domain_url)

        print(str(path))
