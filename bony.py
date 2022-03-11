import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


name = "nadia"
#cori  Fabiana Nadia
#anma
#Esta es una linea nueva d comando
#uno 
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando ... ")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-MX')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except: 
        pass    
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk('Reproduciendo' + music)
        pywhatkit.playonyt(music)
    if 'encuentra' in rec:
        busqueda = rec.replace('encuentra', '')
        talk('Encuentrado' + busqueda)
        pywhatkit.search(busqueda)
    if 'dime la hora' in rec:
        tiempo = datetime.datetime.now().strftime('%I:%M:%p')
        talk('La hora es ' + tiempo)
    if 'busca en wikipedia' in rec:
        autor = rec.replace('busca en wikipedia', '')
        info = wikipedia.summary(autor, 1)
       # print('info')
        talk('Buscando informacion relacionada en wikipedia segun lo indicado' + info)
    if 'broma' in rec:
        talk(pyjokes.get_joke('es'))
    #   else rec.UnknownValueError:
    # si no se entendió
    print("No te pude entender")

run()




