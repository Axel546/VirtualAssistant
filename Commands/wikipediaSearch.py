import wikipedia
import talk as t

def wikiSearch(command):
    person = command.replace('who is', '')
    try:
        info = wikipedia.summary(person, 1)
        print(info)
        t.talk(info)
    except:
        t.talk('I could not find anything on Wikipedia!')