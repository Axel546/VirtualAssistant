import pywhatkit
import talk as t

def play(command):
    song = command.replace('play', '')
    t.talk('playing ' + song)
    print('playing')
    pywhatkit.playonyt(song)