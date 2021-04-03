import speech_recognition as speech
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


class AgainTakeCommand:
    def __init__(self):
        pass

    # text to speech
    def newspeak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

        # take command from user
        # to convert voice into text

    def newCommand(self):
        print("2 nd Recognizer method")
        r = speech.Recognizer()
        with speech.Microphone(device_index=1) as source:
            print('Listening.....')
            r.pause_threshold = 1
            # For Noise
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, timeout=4, phrase_time_limit=7)
            # audio = r.listen(source)  # ,timeout=5,phrase_time_limit=8)

        try:
            print('Recognizing.....')
            text_speech = r.recognize_google(audio, language='en-in')
            print(f'user said :-  {text_speech}')

        except Exception as ex:
            # speak('I don't understand...')
            # speak(f'Sorry Sir, Check Your Internet Connection... ')
            print(ex)
            return 'none'
        text_speech = text_speech.lower()
        return text_speech
