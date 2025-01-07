import time


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

        print()
        print (formatted_time, end="\r",  flush=True)
        # carriage return to replace previous line with new one instead of default line jump

        time_sec+=1

        # wait 1 second before each loop
        time.sleep(1)
        i +=1


# def set_alarm():
    # alarm_time = input("Veuillez entrer l'heure de l'alarme (HH:MM:SS) : ")
    # print("Alarm set for :", alarm_time)

# Run the real-time clock:
# display_time()
# display_time2()

def clock():
    clock_choice = 0
    print("Welcome to granny's clock!")

    while clock_choice != 1 or clock_choice != 2:

        clock_choice = int(input("choose '1: display local time' or '2 : set the clock: "))

    if clock_choice == 1:
        local_time()

    elif clock_choice == 2:
        display_time2()
    
    else:
        print("input error")

 

    
    # keep track of the time in a separate thread
    # import threading
    # thread_time = threading.Thread(target=display_time)
    # thread_time.daemon = True
    # thread_time.start()




if __name__ == "__main__":
    clock()
