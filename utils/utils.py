__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import pyttsx3
import re
import random


class Utils:
    def __init__(self, logger):
        self.logger = logger
        self.engine = pyttsx3.init()

    def playspeak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    # Normalize Utterances using regular expressions
    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for u in utterances:
            normalized += u.lower() + '|'
        return normalized[:-1]  # Slicing here for remove  last | pip

    # Matching utterances
    def match_utterances(self, voice_input, utterances):
        try:
            self.logger.info("Normalizing utterances.........")
            normalized = Utils.normalize_utterances(utterances)
            compile = re.compile(normalized)
            return compile.search(voice_input)
        except Exception as e:
            print(e)


    @staticmethod
    def choose_random(responses):
        return random.choice(responses)
