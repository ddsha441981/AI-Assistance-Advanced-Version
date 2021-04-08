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

import keyboard

from utils.utils import Utils
from utils.speech_recognizes import AgainTakeCommand


class WhatsappMessage:
    def __init__(self, logger, command, response):
        self.logger = logger
        self.command = command
        self.response = response
        self.utils = Utils(self.logger)

    def whatsapp(self,number,msg):
        try:
            numb = "+91" + number
            mess = msg
            open_chat = 'https://web.whatsapp.com/send?phone=' + numb + '&text=' + mess
            webbrowser.open(open_chat)
            time.sleep(15)
            keyboard.press("enter")
        except Exception as ex:
            self.logger.error(ex)

    def opening_whatsapp_msg(self):
        print(self.command)
        query = self.command.split("send whatsapp message")[1].strip()
        self.utils.playspeak("Please Provide Mobile Number....")
        number = str(input("Here..........."))

        self.utils.playspeak("what message do you want to send....")
        msg = AgainTakeCommand.newCommand(self).lower()

        self.logger.info(msg)
        self.whatsapp(number,msg)