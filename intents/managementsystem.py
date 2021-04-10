__author__ = "Deendayal Kumawat"
__version__ = "1.0.1"
__maintainer__ = "Deendayal Kumawat"
__email__ = "codewithcup.developer@gmail.com"
__credits__ = [""]
__copyright__ = ""
__license__ = ""
__status__ = ""

import os
import psutil
import sys
import shutil
import pyautogui
import time
from utils.utils import Utils
from utils.speech_recognizes import AgainTakeCommand


class ManagementSystem:
    def __init__(self, logger, response, system_activities, command, os_name):
        self.logger = logger
        self.response = response
        self.command = command
        self.os_name = os_name
        self.utils = Utils(self.logger)
        self.system_activities = system_activities

    # Response Speak
    def response_speak(self, response):
        self.logger.info(response)
        self.utils.playspeak(response)  # Speak method

    def taking_screenshot_now(self):
        self.response_speak('Sir, Tell me the name for this screenshot file')
        screenshotFile = AgainTakeCommand.newCommand(self).lower()
        self.response_speak('Sir, Please hold the screen for few seconds.., I am taking screenshot')
        time.sleep(5)
        img = pyautogui.screenshot()
        img.save(f'{screenshotFile}.png')
        self.response_speak('Sir,i am done , the screenshot saved in main folder. now i am ready for next command')

    def shutdown(self, time=20):
        print("inside shutdown ")
        """Will shutdown the computer in given seconds
        For Windows and Linux only"""
        if self.os_name == "window":
            cont = "shutdown -s -t %s" % time
            os.system(cont)

        elif self.os_name == "linux":
            cont = "shutdown -h %s" % time
            os.system(cont)

        elif self.os_name == "darwin":
            cont = "shutdown -h -t %s" % time
            os.system(cont)

        else:
            print("This function is for Windows, Mac and Linux users only, can't execute on %s" % self.os_name)

    # restart pc
    def restart_pc(self, time=20):
        if self.os_name == "window":
            os.system('shutdown /r /t 5')

        elif self.os_name == "linux":
            pass

        elif self.os_name == "darwin":
            pass

    # Sleep Pc
    def sleep_pc(self, time=20):
        if self.os_name == "window":
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif self.os_name == "linux":
            pass

        elif self.os_name == "darwin":
            pass

    # Checking Battery Power
    def battery_power(self):
        try:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            self.response_speak(f'Sir our system have {percentage} percentage battery power')

            if percentage >= 75:
                self.response_speak("we have enough power to contiune our work")
            elif percentage >= 40 or percentage <= 75:
                self.response_speak("we should connect our system to charging point to charge our battery")
            elif percentage <= 15 or percentage <= 30:
                self.response_speak("we don't have enough power to contiune work, please connect charging")
            elif percentage <= 15:
                self.response_speak(
                    "we have very low power, Please connect to charging, the system will be shutdown very soon")
        except Exception as e:
            print(e)

    # Checking battery and cpu usage
    def cpu_usage(self):
        # usage = str(psutil.cpu_percent())
        # speak('CPU usage is at ' + usage)
        # print('CPU usage is at ' + usage)

        print('                                                                   ')
        print('----------------------CPU Information summary----------------------')
        print('                                                                   ')

        # gives a single float value
        vcc = psutil.cpu_count()
        print('Total number of CPUs :', vcc)

        usage = str(psutil.cpu_percent())
        vcpu = psutil.cpu_percent()
        print('Total CPUs utilized percentage :', vcpu, '%')
        print('CPU usage is at ' + usage)

        print('                                                                   ')
        print('----------------------RAM Information summary----------------------')
        print('                                                                   ')
        # you can convert that object to a dictionary
        # print(dict(psutil.virtual_memory()._asdict()))
        # gives an object with many fields
        vvm = psutil.virtual_memory()

        x = dict(psutil.virtual_memory()._asdict())

        def forloop():
            for i in x:
                print(i, "--", x[i] / 1024 / 1024 / 1024)  # Output will be printed in GBs

        forloop()
        print('                                                                   ')
        print('----------------------RAM Utilization summary----------------------')
        print('                                                                   ')
        # you can have the percentage of used RAM
        print('Percentage of used RAM :', psutil.virtual_memory().percent, '%')
        # 79.2
        # you can calculate percentage of available memory
        print('Percentage of available RAM :', psutil.virtual_memory().available * 100 / psutil.virtual_memory().total,
              '%')

        print('                                                                   ')
        print('----------------------Battery summary----------------------')
        print('                                                                   ')
        battery = psutil.sensors_battery()
        print("battery is at:" + str(battery.percent))

    # get key from voice input
    def get_path_system(self):
        try:
            if self.command == 'none' or self.command == 'None':
                print("split..................", self.command)
                pass
            else:
                key = self.command.split(' ')[1].strip()
                print('Key is ', key + " command is " + self.command)

                for sysactivity in self.system_activities:
                    print("in for sysactivity is ", sysactivity, "path is : ", sysactivity)
                    if key in sysactivity:
                        return self.system_activities[sysactivity]

        except IndexError as e:
            print(e)
        except Exception:
            pass

    def checking_system_info(self):
        path = self.get_path_system()
        print("check path method ", path)
        self.logger.info('Return path : ' + str(path))
        if str(path) in 'none' or str(path) in 'None':
            print("Inside None...........")
            print("not understand")
        else:
            if path in 'shutdown':
                self.response_speak(self.response)
                self.shutdown(self.os_name)

            elif path in 'restart':
                self.restart_pc()

            elif path in 'sleep':
                self.sleep_pc()

            elif path in 'battery':
                self.battery_power()

            elif path in 'take screenshot' or path in "screenshot":
                self.taking_screenshot_now()

            elif path in 'cpu':
                self.cpu_usage()
            elif path in 'manage files' or path in 'manage data':
                EXT_VIDEO_LIST = ['FLV', 'WMV', 'MOV', 'MP4', 'MPEG', '3GP', 'MKV', 'AVI']
                EXT_IMAGE_LIST = ['JPG', 'JPEG', 'GIF', 'PNG', 'SVG']
                EXT_DOCUMENT_LIST = ['DOC', 'DOCX', 'PPT', 'PPTX', 'PAGES', 'PDF', 'ODT', 'ODP', 'XLSX', 'XLS', 'ODS',
                                     'TXT', 'IN',
                                     'OUT', 'MD']
                EXT_MUSIC_LIST = ['MP3', 'WAV', 'WMA', 'MKA', 'AAC', 'MID', 'RA', 'RAM', 'RM', 'OGG']
                EXT_CODE_LIST = ['CPP', 'RB', 'PY', 'HTML', 'CSS', 'JS']
                EXT_EXECUTABLE_LIST = ['LNK', 'DEB', 'EXE', 'SH', 'BUNDLE']
                EXT_COMPRESSED_LIST = ['RAR', 'JAR', 'ZIP', 'TAR', 'MAR', 'ISO', 'LZ', '7ZIP', 'TGZ', 'GZ', 'BZ2']

                # Taking the location of the Folder to Arrange
                try:
                    destLocation = str(sys.argv[1])
                except IndexError:
                    self.response_speak("Enter the Path of directory")
                    destLocation = str(input('Enter here...... : '))

                # When we make a folder that already exist then WindowsError happen
                # Changing directory may give WindowsError
                def ChangeDirectory(dir):
                    try:
                        os.chdir(dir)
                    except WindowsError:
                        print('Error! Cannot change the Directory')
                        print('Enter a valid directory!')
                        ChangeDirectory(str(input('Enter the Path of directory: ')))

                ChangeDirectory(destLocation)

                def Organize(dirs, name):
                    try:
                        os.mkdir(name)
                        print('{} Folder Created'.format(name))
                    except WindowsError:
                        print('{} Folder Exist'.format(name))

                    src = '{}\\{}'.format(destLocation, dirs)
                    dest = '{}\{}'.format(destLocation, name)

                    os.chdir(dest)
                    shutil.move(src, '{}\\{}'.format(dest, dirs))

                    print(os.getcwd())
                    os.chdir(destLocation)

                TYPES_LIST = ['Video', 'Images', 'Documents', 'Music', 'Codes', 'Executables', 'Compressed']
                for dirs in os.listdir(os.getcwd()):
                    if 1:
                        for name, extensions_list in zip(TYPES_LIST,
                                                         [EXT_VIDEO_LIST, EXT_IMAGE_LIST, EXT_DOCUMENT_LIST,
                                                          EXT_MUSIC_LIST,
                                                          EXT_CODE_LIST, EXT_EXECUTABLE_LIST, EXT_COMPRESSED_LIST]):
                            if dirs.split('.')[-1].upper() in extensions_list:
                                Organize(dirs, name)
                    else:
                        if dirs not in TYPES_LIST:
                            Organize(dirs, 'Folders')
                self.response_speak("task completed..")
                self.response_speak('Done Arranging Files and Folder in your specified directory')

        print(str(path))
