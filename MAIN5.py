import time
from plyer import notification

while True:
    print("Take a sip of some water!")
    notification.notify(title="Please drink some water!",message="It's important to stay hydrated.") # type: ignore
    time.sleep(3600)