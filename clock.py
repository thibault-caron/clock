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


def display_time(clock_sec=None):
    """
    Display the choose time updated every second.
    :return: ∅
    """
    while True:
        print("\r", time.strftime("%H:%M:%S", time.localtime(clock_sec)), end="")
        if clock_sec is not None:
            clock_sec += 1
        time.sleep(1)


def display_menu():
    """
    Display the menu on the terminal.
    :return: ∅
    """
    print("")
    print("Welcome to Grandma's clock!")
    print("In this menu, you can choose between different options:")
    print("")
    print("1: Display current local time")
    print("2: Set the time you want")
    print("3: Set an alarm")
    print("4: Switch between 12 hours and 24 hours display")
    print("5: Pause your clock") 
    print("6: Reset") 
    print("")


def choose_option():
    menu_option = input("Choose your option (enter '1' to '6'): ")

    match menu_option:
        case "1":
            display_time()
        case "2":
            my_clock_sec = seconds_time(clock_input())
            display_time(my_clock_sec)
        case "3":
            print("set the alarm")
        case "4":
            print("switch hour format")
        case "5":
            print("pause the clock")
        case "6":
            clock()
        case _:
            print("Invalid input.")
            choose_option()


def clock():
    """
    Clock main function.
    :return: ∅
    """
    display_menu()
    choose_option()


if __name__ == "__main__":
    clock()
