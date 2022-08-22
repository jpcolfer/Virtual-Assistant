import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'test' in command:
            command = command.replace("Joey", "")
            print(command)

    except:
        pass

    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
    elif "wikipedia" in command:
        person = command.replace("wikipedia", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "note" in command:
        note = command.replace("note", "") + "\n"
        talk("Writing a new note for you saying " + note)
        with open("Notes.txt", "a") as f:
            f.write(note)
    elif "clear" in command:
        talk("Erasing the default notepad.")
        open("Notes.txt", "w").close()
    elif "new" in command:
        name = command.replace("new", "")
        talk("Creating a new notepad called " + name)
        with open(name + ".txt", "w") as f:
            Note = take_command()
            talk("Writing a new note saying " + Note + " in " + name + ".txt")
            f.write(Note)
    elif "list" in command: #Creating a todo list. Should be pretty similar to writing a note except it loops until you're done
        Todo = command.replace("list", "") + "\n"
        talk("Making a to do list. Say done when you are finished")
        with open("ToDo.txt", "w") as f:
            Item = take_command()
            ItemNum = 1
            while Item != "done":
                f.write(str(ItemNum) + ". " + Item + "\n")
                ItemNum+=1
                talk("Task Noted")
                Item = take_command()
            talk("Closing to do list")
    else:
        talk("Please say the command again.")

while True:
    run_alexa()