__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import webbrowser
import time
import keyword
from utils.utils import Utils
from utils.speech_recognizes import AgainTakeCommand


class WhatsappMessage:
    def __init__(self, logger, command, response):
        self.logger = logger
        self.command = command
        self.response = response
        self.utils = Utils(self.logger)

    def whatsapp(self,number,msg):
        numb = number
        mess = msg
        print('https://web.whatsapp.com/send?phone=' + numb + '&text=' + mess)
        open_chat = 'https://web.whatsapp.com/send?phone=' + numb + '&text=' + mess
        print(open_chat)
        webbrowser.open(open_chat)
        time.sleep(15)
        keyword.press("enter")

    def opening_whatsapp_msg(self):
        print(self.command)
        query = self.command.split("send whatsapp message")[1].strip()
        print(query)
        print("whatsapppppp")
        self.utils.playspeak("Please Provide Mobile Number....")
        number = int(input("Here..........."))

        msg = AgainTakeCommand.newCommand(self).lower()
        print(type(number))
        print(msg)
        self.whatsapp(number,msg)

        print("Called")
        # return number

    def hello(self):
        print("jai ho")
