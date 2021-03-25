import os
from utils.utils import Utils


class Application:
    def __init__(self, logger, response, applications, command, os_name):
        self.logger = logger
        self.response = response
        self.command = command
        self.utils = Utils(self.logger)
        self.os_name = os_name
        self.applications = applications

    # get key from voice input
    def get_path(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................",self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
            # Method 1
            # for app in self.applications:
            #     if key in app:
            #         return self.applications[app]

            # Method 2
                for app, path in self.applications.items():
                    if key in app:
                        return path
        except IndexError as e:
            print(e)
        except Exception as e:
            pass

    def launch(self):
        path = self.get_path()
        self.logger.info('Return path : ' + str(path))
        if path:
            self.utils.playspeak(self.response)
            # self.utils.speak(self.response, self.os_name)
            if self.os_name == 'Darwin':
                os.system('open {}'.format(path))
            else:
                # os.system('explorer {}'.format(path))
                os.system('start {}'.format(path))
        else:
            self.utils.playspeak('I am sorry Sir. The app which you are looking for, is not register into my database.')
        # os.system('explorer {}'.format(path))
