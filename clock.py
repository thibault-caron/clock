import time


def display_time():
    while True:
        # initialize time variable (from local time)
        current_time = time.localtime()

        # format time as: hh:mm:ss
        formatted_time = time.strftime("%H:%M:%S", current_time)

        print ("\r", formatted_time, end="",  flush=True)    # carriage return to replace previous line with new one, end="" to remove default line jump

        # wait 1 second before each loop
        time.sleep(1)

###############################################################


def display_time2():
    input_time = input("What time is it? Use the format 'hours:minutes:seconds': ").split(":")
    tuple_time = tuple(input_time)
    time_sec = (int(tuple_time[0])*3600 + int(tuple_time[1])*60 + int(tuple_time[2])) - 3600 
    i = 0
    while i < 120:

        # format time as: hh:mm:ss
        formatted_time = time.strftime("%H:%M:%S", time.localtime(time_sec))
        # formatted_time = time.strftime("%H:%M:%S", tuple_time)

        print ("\r", formatted_time, end="",  flush=True)   # carriage return to replace previous line with new one, end="" to remove default line jump
        time_sec+=1

        # wait 1 second before each loop
        time.sleep(1)
        i +=1


# def set_alarm():

# Run the real-time clock:
# display_time()
display_time2()
