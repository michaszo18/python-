import time
import winsound

from win10toast import ToastNotifier


class WindowsToast():

    def __init__(self, message, minutes=1):
        self.message = message
        self.minutes = minutes

    def start(self):
        notificator = ToastNotifier()
        # notificator.show_toast("Alarm", f"Alarm will go off {self.minutes} minutes", duration=10)
        time.sleep(self.minutes * 60)
        winsound.Beep(2500, 1000)
        notificator.show_toast("Alarm", self.message, duration=50)


windowsToast = WindowsToast("Jo ryju", 1/60)
windowsToast.start()