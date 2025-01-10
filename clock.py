"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 10/01/2025 11h38
Aim of the program :
    Display the clock.
Input : clock :
Output :
"""

from time import sleep
from datetime import datetime, timedelta
from os import system, name


def clock_input():
    """
    Function used to set the clock.
    :return: A tuple of hours, minutes and seconds user has chose.
    """
    test = False
    while not test:
        try:
            clock_h = int(input("\nFirst, choose hours (24h format only) : ", ))
            if 0 <= clock_h < 24:
                test = True
            else:
                print("\nHour has to be in a correct range!")
        except ValueError:
            print("\nWhat have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while test:
        try:
            clock_m = int(input("Next, choose minutes : ", ))
            if 0 <= clock_m < 60:
                test = False
            else:
                print("\nMinutes has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test:
        try:
            clock_s = int(input("And at the end, choose seconds : ", ))
            if 0 <= clock_s < 60:
                test = True
            else:
                print("\nSeconds has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    return clock_h, clock_m, clock_s


def clock_now():
    """
    Function used to return computer time.
    :return: A tuple of hours, minutes and seconds.
    """
    clock_h = datetime.now().hour
    clock_m = datetime.now().minute
    clock_s = datetime.now().second
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
                print("\nYou can only choose 1 or 2")
        except ValueError:
            print("\nUse only integers numbers")


def display_time(alarm, clock, hour_format):
    """
    Display the choose time updated every second.
    When clock is set at None display curent time.
    :param alarm: A datetime formated alarm.
    :param clock: A tuple of hours, minutes and seconds.
    :param hour_format: Hour display format (24h or 12h with AM/PM).
    :return: ∅
    """
    clock_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, clock[0], clock[1], clock[2])
    increment = timedelta(seconds=1)

    while True:
        if hour_format == 24:
            print(f"\r{clock_time.strftime("%H:%M:%S")}", end="")
        else:
            print(f"\r{clock_time.strftime("%I:%M:%S %p")}", end="")

        if alarm is not None:
            if alarm == clock_time:
                print("\nWake up quick!!\nThe Wolf is near your house!")

        clock_time = clock_time + increment
        sleep(1)


def cls():
    """
    Clear the console on Windows or Linux OS.
    :return: ∅
    """
    system('cls' if name == 'nt' else 'clear')


def choose_option(alarm_time, clock_format, view_menu=True):
    """
    Take and execute the function the user wants.
    Use the function display_menu.
    :return: ∅
    """

    def display_menu():
        """
        Display the menu on the terminal.
        :return: ∅
        """
        print("\n1: Display current local time")
        print("2: Set the time you want")
        print("3: Set an alarm")
        print("4: Switch between 12 hours and 24 hours display")
        print("5: Pause your clock")
        print("6: Exit\n")

    if view_menu is True:
        display_menu()
    menu_option = input("Choose your option (enter '1' to '6'): ")

    match menu_option:
        case "1":
            computer_time = clock_now()
            display_time(alarm_time, computer_time, clock_format)
        case "2":
            print("\nSet the clock!")
            user_time = clock_input()
            display_time(alarm_time, user_time, clock_format)
        case "3":
            print("\nSet the alarm!")
            alarm_tuple = clock_input()
            alarm_time = datetime(datetime.now().year, datetime.now().month,datetime.now().day,
                                  alarm_tuple[0], alarm_tuple[1], alarm_tuple[2])
            choose_option(alarm_time, clock_format)
        case "4":
            print("\nHour format switched!")
            clock_format = 12 if clock_format == 24 else 24
            print(f"Now the clock is set in {clock_format} hours")
            choose_option(alarm_time, clock_format,False)
        case "5":
            print("\nClock paused")
            choose_option(alarm_time, clock_format,False)
        case "6":
            cls()
            exit()
        case _:
            print("Invalid input!\nDon't do that! The wolf is coming!")
            choose_option(alarm_time, clock_format, False)


def clock(): 
    """
    Clock main function.
    :return: ∅
    """
    try:
        clock_format_default = 24
        alarm_default = None

        print("\nWelcome to Grandma's clock!\n")
        print("In this menu, you can choose between different options:")

        choose_option(alarm_default, clock_format_default)

    except KeyboardInterrupt:
        cls()
        clock()


if __name__ == "__main__":
    clock()
