import keyboard
import pyautogui
from utils.utils import Utils
from utils.speech_recognizes import AgainTakeCommand


class AutomateAnyThing:
    def __init__(self, logger, response, automate_tool, command):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.automate_tool = automate_tool

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    # Youtube Automation
    def youtubeAuto(self):
        self.response_speak("Whats Your Command ?")
        comm = AgainTakeCommand.newCommand(self).lower()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        self.response_speak("Done Sir")

    # Chrome Automation
    def chromeAuto(self):
        self.response_speak("Chrome Automation started!")

        command = AgainTakeCommand.newCommand(self).lower()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')

    # get key from voice input
    def get_path_automate(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is', key + " command is " + self.command)

                for automate in self.automate_tool:
                    print("in for activity is ", automate, "path is : ", automate)
                    if key in automate:
                        return self.automate_tool[automate]

        except IndexError as e:
            print(e)
        except Exception:
            pass

    def opening_automate_data(self):
        path = self.get_path_automate()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'youtube':
                self.response_speak(self.response)
                self.youtubeAuto()

            elif path in 'chrome':
                self.response_speak(self.response)
                self.chromeAuto()

            elif path in 'up' or path in 'volumeup' or path in 'volume up':
                self.response_speak('ok volume up')
                pyautogui.press("volumeup")

            elif path in 'down' or path in 'volumedown' or path in 'volume down':
                self.response_speak('ok volume down')
                pyautogui.press("volumedown")

            elif path in 'mute' or path in 'volumemute' or path in 'volume mute':
                self.response_speak('ok volume mute')
                pyautogui.press("volumemute")

            elif path in 'pause':
                pass

        print(str(path))
