import takeCommand as take
import talk as t
from Commands import *


def run():
    command = take.take_command()
    print(command)
    if 'play' in command:
        playYoutube.play(command)
    elif 'time' in command:
        askTime.askForTime()
    elif 'who is' in command:
        wikipediaSearch.wikiSearch(command)
    elif 'joke' in command:
        ok = 0
        if 'chuck' in command:
            ok = 1
        jokeTelling.tellJoke(ok)
    elif 'stop' in command:
        stop.end()
    else:
        t.talk('Please say the command again.')
