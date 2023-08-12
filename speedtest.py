from pynput import keyboard
import time
def typing_speed():
    typing1=0
    possible=0
    time_list=[time.time()]
    with keyboard.Events() as events:
        while True:
            tpying=events.get(0.01)
            if tpying is not None:
                time_list.append(time.time())
                typing1+=1
                if time_list[typing1]-time_list[typing1-1]<0.03:
                    possible+=1

            if len(time_list)>100:
                time_list.clear()
                time_list=[time.time()]
                typing1=-1
                typing2=0

            if possible>=10:
                return True
                break
        

#typing_speed() 