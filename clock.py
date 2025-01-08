"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 08/01/2025 17h22
Aim of the program :
    Display the clock.
Input : clock :
Output :
"""

import time
import datetime


def clock_input():
    """
    Function used to set the clock.
    :return: A tuple of hours, minutes and seconds user has chose.
    """
    test1 = False
    test2 = False
    test3 = False
    while not test1:
        try:
            clock_h = int(input("Set the clock!\n\nFirst, choose hours : ", ))
            if 0 <= clock_h < 24:
                test1 = True
            else:
                print("Hour has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test2:
        try:
            clock_m = int(input("Next, choose minutes : ", ))
            if 0 <= clock_m < 60:
                test2 = True
            else:
                print("Minutes has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test3:
        try:
            clock_s = int(input("And at the end, choose seconds : ", ))
            if 0 <= clock_s < 60:
                test3 = True
            else:
                print("Seconds has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    return clock_h, clock_m, clock_s


def seconds_time(clock):
    """
    Convert a tuple of hours, minutes and seconds only in seconds.
    :param clock: A tuple of hours, minutes and seconds.
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


def display_time(clock=None):
    """
    Display the choose time updated every second.
    When clock is set at None display curent time.
    :param clock: A tuple of hours, minutes and seconds.
    :return: ∅
    """
    if clock is None:
        clock_time = datetime.datetime.now()
    else:
        clock_time = datetime.datetime(1900, 1, 1, clock[0], clock[1], clock[2])
        clock_sec = datetime.timedelta(seconds=1)

    while True:
        print("\r", f"{clock_time.hour}:{clock_time.minute}:{clock_time.second}", end="")
        if clock is not None:
            clock_time = clock_time + clock_sec
        time.sleep(1)


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
        my_clock_sec = clock_input()
        display_time(my_clock_sec)
    else:
        display_time()


if __name__ == "__main__":
    clock()
