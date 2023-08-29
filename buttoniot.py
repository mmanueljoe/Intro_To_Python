from gpiozero import Button
from signal import pause
from sendmessage import IftttNotification

event = "send an email"
api_key = "oV6v6-_PeKoO-auEhzrJHB4unVjMA1H4KtSI5oPAaxf"
jd = {"Firstname":"Emmanuel","Lastname": "Letsu","Age": 23,"Complextion":"Brown"}

IfNot = IftttNotification(event,api_key)



# button = Button(2)

# button.wait_for_press()
# print("Button is pressed")

# def say_hello():
#     print("Hello")

def theFunc():
    return IfNot.notify(jd)

button1 = Button(2)

button1.when_pressed = theFunc

pause()