from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("setting up alarm...")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    curr_minute = now.strftime("%M")
    curr_seconds = now.strftime("%S")
    curr_period = now.strftime("%p")
    print(current_hour)
    if alarm_period == curr_period :
        if alarm_seconds == curr_seconds :
            if alarm_hour == current_hour :
                if alarm_minute == curr_minute :
                    print("Wake Up!!")
                    playsound('audio.ogg')
                    break
