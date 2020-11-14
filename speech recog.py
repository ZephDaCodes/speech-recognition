def voicetotext():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Please input speech")
        audio=r.listen(source)
    result=""

    try:
        result=r.recognize_google(audio)
    except sr.UnknownValueError:
        print("No audio input")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))

    return result

def texttovoice(csin):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(csin)
    engine.runAndWait()
    
while 1:
    csin=voicetotext()
    if csin==("exit") or csin==("quit") or csin == "bye":
        break
    else:
        texttovoice(csin)
    
