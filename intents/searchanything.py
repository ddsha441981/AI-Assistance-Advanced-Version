import webbrowser
class SearchAnything:
    def __init__(self,logger,command):
        self.logger = logger
        self.command = command

    def searching_on_google(self):
        voicenote = self.command.split("ok google")[1].strip()
        webbrowser.open("https://www.google.com/search?q={}".format(voicenote))


