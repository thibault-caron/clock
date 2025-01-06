import time
import datetime

#program that displays a naive time and refresh in reel time
#dt = time.localtime()
#print(dt.strftime('%H:%M:%S'))

while True:
# initialize time variable 
    current_time = time.localtime()

# format time as : hh:mm:ss
    formatted_time = time.strftime("%H:%M:%S", current_time)

    print("\r", formatted_time, end="", flush=True)

    time.sleep(1)
    