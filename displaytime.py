import time
import datetime

#program that displays a naive time and refresh in reel time
#dt = time.localtime()
#print(dt.strftime('%H:%M:%S'))

# while True:
# # initialize time variable 
#     current_time = time.localtime()

# # format time as : hh:mm:ss
#     formatted_time = time.strftime("%H:%M:%S", current_time)

# # refresh time every second
#     print("\r", formatted_time, end="", flush=True)

#     time.sleep(1)

# other solution : 
# fonction to set time :
def display_time():

    # input current time with number of hours, of minutes :
    h = int(input('Enter current hour (without minutes) :'))
    m = int(input('Enter current minute : '))

    # calculation of timestamp (less one hour because of 1 am start) :
    i = (h*3600) + (m*60) - 3600

    # loop for refresh time every second :
    while True:
        print ("\r", time.strftime("%H:%M:%S", time.localtime(i)), end="")
        i = i+1
        time.sleep(1)

display_time()

    