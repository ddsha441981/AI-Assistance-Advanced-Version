__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import webbrowser
import requests
from utils.utils import Utils
import wikipedia as googleScrap
import wikipedia


class SearchAnything:
    def __init__(self, logger, response, online_content, command):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.online_content = online_content

    def searching_on_google(self):
        searchQuery = self.command.split("ok google")[1].strip()
        try:
            webbrowser.open("https://www.google.com/search?q={}".format(searchQuery))
            result = googleScrap.summary(searchQuery,2)
            self.response_speak(result)
        except Exception as e:
            self.response_speak("No Speakable Data found............")
            self.logger.error(e)

    def searching_on_youtube(self):
        topic = self.command.split("play youtube video")[1].strip()

        url = 'https://www.youtube.com/results?q=' + topic
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count - 5] == "/results":
            raise Exception("No video found.")

        webbrowser.open("https://www.youtube.com" + lst[count - 5])
        return "https://www.youtube.com" + lst[count - 5]

    def searching_on_wikipedia(self):
        try:
            wikitext = self.command.split("search wikipedia")[1].strip()
            wiktext = wikipedia.summary(wikitext, sentences=3)
            self.response_speak("According to wikipedia!!!")
            self.response_speak(wiktext)
        except Exception as ex:
            self.logger.error(ex)

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    # get key from voice input
    def get_path_online(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is', key + " command is " + self.command)

                for onlinedata in self.online_content:
                    print("in for activity is ", onlinedata, "path is : ", onlinedata)
                    if key in onlinedata:
                        return self.online_content[onlinedata]

        except IndexError as e:
           self.logger.error(e)
        except Exception as ee:
            self.logger.error(ee)

    def searching_online_content(self):
        path = self.get_path_online()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'google':
                self.response_speak(self.response)
                self.searching_on_google()

            elif path in 'youtube' or path in 'video':
                self.response_speak(self.response)
                self.searching_on_youtube()

            elif path in 'wikipedia' or path in 'search':
                self.response_speak(self.response)
                self.searching_on_wikipedia()

            elif path in 'youtube automation':
                self.youtubeAuto()

        print(str(path))
