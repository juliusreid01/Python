import winsound
import time

# implements a general purpose event scheduler
import sched

def my_alarm(alarmTime, alarmSound, msg):
    while time.time() <= alarmTime: time.sleep(0.1)
    #winsound.Beep(2500, 1000)
    print(msg)
    winsound.PlaySound(alarmSound, winsound.SND_FILENAME)

def set_alarm(alarmTime, alarmSound, msg):
    # scheduler object
    s = sched.scheduler(time.time, time.sleep)
    # schedule the events
    s.enterabs(alarmTime, 1, print, argument=(msg))
    s.enterabs(alarmTime, 1, print, argument=(msg,))
    s.enterabs(alarmTime, 1, winsound.PlaySound, argument=(alarmSound, winsound.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(alarmTime)))
    print('Current time', time.asctime(time.localtime(time.time())))
    s.run()
    
#print("Running my alarm ...")
#my_alarm(time.time()+1,'alarm.wav',"Hello World!")
set_alarm(time.time()+2,'alarm.wav',"Hello World!")
