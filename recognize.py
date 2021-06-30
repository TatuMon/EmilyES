import speech_recognition as sr
import commands

recognizer = sr.Recognizer()

def voiceToText():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Analizando audio...")
            text = recognizer.recognize_google(audio, language="es-AR")
            return text
        except:
            return("")

def wordIdentifier(request:list):
    words = request.split(' ')
    commands.activateCommand(words)