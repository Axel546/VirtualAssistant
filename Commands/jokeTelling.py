import pyjokes
import talk as t

def tellJoke(ok):
    if ok == 1:
        t.talk(pyjokes.get_joke('en','chuck'))
    else:
        t.talk(pyjokes.get_joke('en', 'all'))