import time


def display_time():
    while True:
        current_time = time.localtime()
        formatted_time = time.strftime("%H:%M:%S", current_time)
        print (formatted_time, end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(1)


# def set_alarm():

display_time()
