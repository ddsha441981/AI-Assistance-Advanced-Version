import json
import logging
from assistant.jarvis import Jarvis
import os
import platform
import sys
from PyQt5.QtWidgets import QApplication
from assistant.gui import GUI


# reading json file
def read_json_file():
    logging.info("Reading configuration file....1")
    with open("config/config.json") as file:
        return json.load(file)


# reading json file
def read_json_files():
    logging.info("Reading configuration file....2")
    with open("config/searchAnything.json") as f:
        return json.load(f)


if __name__ == '__main__':
    operating_system = platform.uname().system
    # print(operating_system)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%y-%m-%d %H:%M:%S')

    logging.info("Jarvis is initializing..............")
    jarvis = Jarvis(logger=logging, config=read_json_file(), os_name=operating_system)
    # jarvis = Jarvis(logger=logging, config=read_json_files(), os_name=operating_system)

    app = QApplication(sys.argv)
    gui = GUI()
    jarvis.start()
    gui.start()

    app.exit(app.exec_())
