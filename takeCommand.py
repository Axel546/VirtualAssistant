import speech_recognition as sr

listener = sr.Recognizer()

def take_command():
    try:
        command = 'Try again!'
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command
