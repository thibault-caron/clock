"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 09/01/2025 14h57
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
            clock_h = int(input("\nFirst, choose hours : ", ))
            if 0 <= clock_h < 24:
                test1 = True
            else:
                print("\nHour has to be in a correct range!")
        except ValueError:
            print("\nWhat have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test2:
        try:
            clock_m = int(input("Next, choose minutes : ", ))
            if 0 <= clock_m < 60:
                test2 = True
            else:
                print("\nMinutes has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test3:
        try:
            clock_s = int(input("And at the end, choose seconds : ", ))
            if 0 <= clock_s < 60:
                test3 = True
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
    clock_h = datetime.datetime.now().hour
    clock_m = datetime.datetime.now().minute
    clock_s = datetime.datetime.now().second
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


def display_time(alarm, clock):
    """
    Display the choose time updated every second.
    When clock is set at None display curent time.
    :param alarm: A datetime formated alarm.
    :param clock: A tuple of hours, minutes and seconds.
    :return: ∅
    """
    clock_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
                                   datetime.datetime.now().day, clock[0], clock[1], clock[2])
    increment = datetime.timedelta(seconds=1)

    while True:
        print("\r", clock_time.strftime("%H:%M:%S"), end="")

        if alarm is not None:
            if alarm == clock_time:
                print("\nWake up quick!!\nWolf is near your house!")
        clock_time = clock_time + increment
        time.sleep(1)


def cls():
    """
    Clear the console on Windows or Linux OS.
    :return: ∅
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """
    Display the menu on the terminal.
    :return: ∅
    """
    print("\nWelcome to Grandma's clock!\n")

    print("In this menu, you can choose between different options:\n")

    print("1: Display current local time")
    print("2: Set the time you want")
    print("3: Set an alarm")
    print("4: Switch between 12 hours and 24 hours display")
    print("5: Pause your clock")
    print("6: Exit\n")


def choose_option(alarm_time):
    """
    Take and execute the function the user wants.
    :return: ∅
    """
    menu_option = input("Choose your option (enter '1' to '6'): ")

    match menu_option:
        case "1":
            computer_time = clock_now()
            display_time(alarm_time, computer_time)
        case "2":
            print("\nSet the clock!")
            user_time = clock_input()
            display_time(alarm_time, user_time)
        case "3":
            print("\nSet the alarm!")
            alarm_tuple = clock_input()
            alarm_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
                                           datetime.datetime.now().day, alarm_tuple[0], alarm_tuple[1], alarm_tuple[2])
            display_menu()
            choose_option(alarm_time)
        case "4":
            print("\nHour format switched!")
            display_menu()
            choose_option(alarm_time)
        case "5":
            print("\nClock paused")
            display_menu()
            choose_option(alarm_time)
        case "6":
            cls()
            exit()
        case _:
            print("Invalid input!\nDon't do that! The wolf it's coming!")
            choose_option(alarm_time)


def clock():
    """
    Clock main function.
    :return: ∅
    """
    try:
        alarm_default = None
        display_menu()
        choose_option(alarm_default)
    except KeyboardInterrupt:
        cls()
        clock()


if __name__ == "__main__":
    clock()

# binary_choice et seconds_time ne sont plus utilisés (pour le moment)

# Piste de remplacement pour display_time()

# def display_time():
#     """
#     Display the choose time updated every second.
#     :return: ∅
#     """
#     while True:
#         if alarm_time == user_time:
#             print("\r", clock, "ALARM RINGING!", end="")
#         else:
#             print("\r", clock, end="")
#         time.sleep(1)


# def passing_time(clock):
#     """
#     Keep track of the passing time
#     :return: user_time
#     """
#     while True:
#         clock += 1
#         time.sleep(1)
