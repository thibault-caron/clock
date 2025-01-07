"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 06/01/2025 15h37
Aim of the program :
    Display the clock.
Input : clock :
Output :
"""

import time


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


# clock_in = 12, 25, 37
"""
clock_in = clock_input()
clock_sec = clock_in[0] * 3600 + clock_in[1] * 60 + clock_in[2]
clock_sec = clock_sec - 3600  # Correct time because it begins at 1:00 AM
while True:
    print("\r", time.strftime("%H:%M:%S", time.localtime(clock_sec)), end="")
    clock_sec += 1
    time.sleep(1)
"""


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


def current_time():
    """
    Display the current time updated every second.
    :return: ∅
    """
    while True:
        print("\r", time.strftime("%H:%M:%S", time.localtime()), end="")
        time.sleep(1)


def user_time():
    """
    Display the time chosen by the user updated every second.
    :return: ∅
    """
    clock_in = clock_input()
    clock_sec = clock_in[0] * 3600 + clock_in[1] * 60 + clock_in[2]
    clock_sec = clock_sec - 3600  # Correct time because it begins at 1:00 AM
    while True:
        print("\r", time.strftime("%H:%M:%S", time.localtime(clock_sec)), end="")
        clock_sec += 1
        time.sleep(1)


def clock():
    """
    Clock main function.
    :return: ∅
    """
    print("Do you want to set the clock time or use current time?\nChoose 1 to set your time or 2 to use current time.")
    my_choice = binary_choice()
    if my_choice == 1:
        user_time()
    elif my_choice == 2:
        current_time()


if __name__ == "__main__":
    clock()