import time
import datetime

################################################

def local_time():
    while True:
        # initialize time variable (from local time)
        current_time = time.localtime()

        # format time as: hh:mm:ss
        formated_time = time.strftime("%H:%M:%S", current_time)

        print (formated_time, end="\r",  flush=True)
        # carriage return to replace previous line with new one instead of default line jump

        # wait 1 second before each loop
        time.sleep(1)
        # return formated_time

##################################################

def display_time2():
    input_time = input("What time is it? Use the format 'hours:minutes:seconds': ").split(":")
    tuple_time = tuple(input_time)
    time_sec = (int(tuple_time[0])*3600 + int(tuple_time[1])*60 + int(tuple_time[2])) - 3600
    # format time as: hh:mm:ss
    formatted_time = time.strftime("%H:%M:%S", time.localtime(time_sec))


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


    