import datetime
import talk as t

def askForTime():
    time = datetime.datetime.now().strftime('%H:%M')
    t.talk('Current time is ' + time)