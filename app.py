import speech_recognition as sr

def recognize_speech():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something using your microphone:")
        
        # Listen to the user's choice
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    # Use the default microphone as the audio source
    while True:
        try:
            value = recognizer.recognize_google(audio, language="en-US") #language="fr-FR"
            print(value)
            break
        except sr.UnknownValueError:
            print('Could not understand audio')
            return "i could not understand audio"
        except sr.RequestError as e:
            print('Could not request results from my service; {0}'.format(e))
            return "Could not request results from my service; {0}".format(e)
        except Exception as e:
            print('An error occured'),e
            return "An error occurred:", e

# ANSI escape sequence for bold and grey (bright black)
bold_grey = '\033[1;90m'
reset = '\033[0m'

print(f'{bold_grey}-------------------------------------------------------------{reset}')
print(f'{bold_grey}|                         SPEECH TO TEXT                    |{reset}')
print(f'{bold_grey}|                            MADE BY                        |{reset}')
print(f'{bold_grey}|           SOYAM KAPOOR, MUHAMMAD USMAN, ASMA CHANNA       |{reset}')
print(f'{bold_grey}-------------------------------------------------------------{reset}')
recognize_speech()