from datetime import datetime
from win10toast import ToastNotifier
import time


starttime = time.time()
print('Starting')
while True:
    # Remind to look away
    
    time.sleep(20*60)
    toaster = ToastNotifier()
    toaster.show_toast("Take a break")
    time.sleep(2 * 60)
    toaster.show_toast("Break's over")
    
