import pyttsx3
import requests
import speech_recognition

class VoiceAssistant:
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""

def joke_recognition():
    try:
        res = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
        string = res.text
        index2 = string.find('flags')
        index = string.find('joke')
        if index == -1:
            index = string.find('setup')
            index1 = string.find('delivery')
            setup = string[index + 9:index1 - 8].replace('/', ' ')
            delivery = string[index1 + 12:index2 - 8].replace('/', ' ')
            return {setup, delivery}
        else:
            joke = string[index + 8:index2 - 8].replace('/', ' ')
            return {joke}
    except Exception as e:
        print("Exception :", e)
        pass


def setup_assistant_voice():
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        ttsEngine.setProperty("voice", voices[0].id)

def record_and_recognize_audio(*args: tuple):

    with microphone:

        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data

def play_voice_assistant_speech(text_to_speech):
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()

if __name__ == "__main__":
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    ttsEngine = pyttsx3.init()

    assistant = VoiceAssistant()
    assistant.name = "Anny"
    assistant.sex = "female"
    assistant.speech_language = "en"

    setup_assistant_voice()

    while True:

        voice_input = record_and_recognize_audio()
        print(voice_input)
        command = voice_input

        if command == "привет":
            play_voice_assistant_speech("Hi, how are you?")

        if command == "как тебя зовут":
            play_voice_assistant_speech("My name is Andrey, i'm voice assistent!")

        if command == "что ты умеешь":
            play_voice_assistant_speech("I can tell you a lot of jokes.")

        if command == "расскажи шутку":
            arr = joke_recognition()
            for elem in arr:
                play_voice_assistant_speech(elem)

        if command == "следующия шутка":
            arr = joke_recognition()
            for elem in arr:
                play_voice_assistant_speech(elem)

        if command == "выведи шутку":
            arr = joke_recognition()
            for elem in arr:
               print(elem)

        if command == "расскажи две шутки" or command == "расскажи 2 шутки":
            play_voice_assistant_speech("First Joke")
            arr = joke_recognition()
            for elem in arr:
                play_voice_assistant_speech(elem)

            play_voice_assistant_speech("Second Joke")
            arr = joke_recognition()
            for elem in arr:
                play_voice_assistant_speech(elem)

        if command == "спасибо":
            play_voice_assistant_speech("You welcome")

        if command == "пока":
            play_voice_assistant_speech("See you later, goodbye!")
            ttsEngine.stop()
            quit()