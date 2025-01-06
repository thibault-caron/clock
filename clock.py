import time

def display_time():
    while True:
        # initialize time variable (from local time)
        current_time = time.localtime()

        # format time as: hh:mm:ss
        formatted_time = time.strftime("%H:%M:%S", current_time)

        print ("\r", formatted_time, end="",  flush=True)    # carriage return to replace previous line with new one

        # wait 1 second before each loop
        time.sleep(1)


# def set_alarm():

# Run the real-time clock:
display_time()
