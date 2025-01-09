"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 06/01/2025 15h37
Aim of the program :
    Display the clock.
Input : clock :
Output :
"""

import time

my_alarm_sec = 0


def clock_input():
    """
    Function used to set the clock.
    :return: A tuple of hours, minutes and seconds user has chose.
    """
    test = False
    while not test:
        try:
            clock = (int(input("Set the clock!\n\nFirst, choose hours : ", )), int(input("Next, choose minutes : ", )),
                     int(input("And at the end, choose seconds : ", )))
            if 0 <= clock[0] < 24:
                if 0 <= clock[1] < 60:
                    if 0 <= clock[2] < 60:
                        return clock
                    else:
                        print("Seconds has to be in a correct range!")
                else:
                    print("Minutes has to be in a correct range!")
            else:
                print("Hour has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\nGrandma has been eaten by a wolf!!\n")


def seconds_time(clock):
    """
    Convert a tuple of hours, minutes and seconds only in seconds.
    :return: Time in seconds.
    """
    clock_sec = clock[0] * 3600 + clock[1] * 60 + clock[2]
    clock_sec = clock_sec - 3600  # Correct time because it begins at 1:00 AM
    return clock_sec


def binary_choice():
    """
    Translate a choice in integers 1 or 2.
    :return: Integer 1 or 2.
    """
    test = False
    while not test:
        try:
            binary = int(input("Your choice: ", ))
            if binary == 1 or binary == 2:
                return binary
            else:
                print("You can only choose 1 or 2")
        except ValueError:
            print("Use only integers numbers")


def display_time(clock_sec=0):
    """
    Display the choose time updated every second.
    :return: ∅
    """
    if clock_sec == 0:
        clock_sec = None

    while True:
        print("\r", time.strftime("%H:%M:%S", time.localtime(clock_sec)), end="")
        if clock_sec is not None:
            clock_sec += 1
        time.sleep(1)

def check_alarm ()
    tps = time.strftime("%H:%M:%S", time.localtime(clock_sec)) 
    



def clock():
    """
    Clock main function.
    :return: ∅
    """
    print("Do you want an alarm ?\nChoose 1 to set your alarm time or 2 to pass the step.")
    my_choice = binary_choice()
    if my_choice == 1:
        my_alarm_sec = seconds_time(clock_input())
    
    print("Do you want to set the clock time or use current time?\nChoose 1 to set your time or 2 to use current time.")
    my_choice = binary_choice()
    if my_choice == 1:
        my_clock_sec = seconds_time(clock_input())
        display_time(my_clock_sec)
    else:
        display_time()






if __name__ == "__main__":
    clock()