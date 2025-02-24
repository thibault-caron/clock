"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 13/01/2025 8h48
Aim of the program :
    Display the clock.
Inputs : The user enter the menu's option he has chosen and if necessary he set clock time and alarm time.
Output : Display a menu were you can choose option to run the clock.
"""

from time import sleep
from datetime import datetime, timedelta
from os import system, name
from keyboard import is_pressed


def clock_input():
    """
    Function used to set the clock.
    Use the function time_input.
    :return: A tuple of hours, minutes and seconds user has chose.
    """

    def time_input(value, limit):
        """
        Function used to input one of the clock parameters (hours, minutes or seconds).
        :param value: The time parameter to input.
        :param limit: Maximum value of the parameter (23 for hour, 59 for minutes and seconds).
        :return: Time parameter input.
        """
        test = False
        while not test:
            try:
                clock = int(input(f"Choose the {value} : "))
                if 0 <= clock <= limit:
                    test = True
                else:
                    print(f"\nThe {value} have to be in a correct range! (00-{limit})")
            except ValueError:  # Create an exception when the user doesn't enter an integer.
                print("\nWhat have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")
        return clock

    clock_h = time_input("hours", 23)
    clock_m = time_input("minutes", 59)
    clock_s = time_input("seconds", 59)

    return clock_h, clock_m, clock_s  # Return a tuple of hours, minutes and seconds.


def clock_now():
    """
    Function used to return computer time.
    :return: A tuple of hours, minutes and seconds.
    """
    clock_h = datetime.now().hour
    clock_m = datetime.now().minute
    clock_s = datetime.now().second

    return clock_h, clock_m, clock_s  # Return a tuple of hours, minutes and seconds.


def display_time(alarm, clock, hour_format, paused=False):
    """
    Display the chosen time updated every second.
    When clock is set at None, display the current time.
    :param alarm: A datetime formatted alarm.
    :param clock: A tuple of hours, minutes and seconds.
    :param hour_format: Hour display format (24h or 12h with AM/PM).
    :param paused: Used to pause the clock.
    :return: ∅
    """

    clock_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, clock[0], clock[1], clock[2])
    increment = timedelta(seconds=1)  # Create a one-second step to increment the time.

    print("\nClock will run\nUse the 'space' key to stop the clock and resume it.\n"
          "Use the 'KeyboardInterrupt' key (ctrl+c) to come back to the clock menu (all options will be reset).\n")

    while True:
        if is_pressed('space'):  # Check if the space key is pressed.
            paused = not paused  # Toggle the paused state.
            print(f"\nClock {'paused' if paused else 'resumed'}!")
            sleep(0.5)  # Debounce the key press to avoid toggling multiple times in one press.

        if paused:
            continue  # Skip the rest of the loop until resumed.

        if hour_format == 24:
            print(f"\r{clock_time.strftime('%H:%M:%S')}", end="")  # Print time in 24h format (16:25:10).
        else:
            print(f"\r{clock_time.strftime('%I:%M:%S %p')}", end="")  # Print time in 12h format (04:25:10 PM).

        if alarm is not None:
            if alarm == clock_time:  # Checks if it is alarm time.
                print("\nWake up quick!!\nThe Wolf is near your house!")

        clock_time = clock_time + increment
        sleep(1)  # Wait a second before updating the time.


def cls():
    """
    Clear the console on Windows or Linux OS.
    :return: ∅
    """
    system('cls' if name == 'nt' else 'clear')  # Check computer and choose the correct clear command.


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
        print("5: Exit\n")

    if view_menu is True:  # Check if the clock menu has to be displayed.
        display_menu()  # Display the clock menu.
    menu_option = input("Choose your option (enter '1' to '5'): ")

    match menu_option:
        case "1":  # The user chose to display computer time.
            computer_time = clock_now()
            display_time(alarm_time, computer_time, clock_format)  # Display the clock.

        case "2":  # The user chose to set the clock time to display.
            print("\nSet the clock!")
            user_time = clock_input()
            display_time(alarm_time, user_time, clock_format)  # Display the clock.

        case "3":  # The user chose to set an alarm.
            print("\nSet the alarm!")
            alarm_tuple = clock_input()  # A tuple of hours, minutes, and seconds.
            alarm_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                  alarm_tuple[0], alarm_tuple[1], alarm_tuple[2])  # Transform tuple in datetime object.
            choose_option(alarm_time, clock_format)  # Come back to the choice of menu options and display the menu.

        case "4":  # The user chose to change hours format.
            print("\nHour format switched!")
            clock_format = 12 if clock_format == 24 else 24
            print(f"Now the clock is set in {clock_format} hours\n")
            choose_option(alarm_time, clock_format, False)  # Come back to choice of menu options.

        case "5":  # The user chose to exit the program.
            cls()
            exit()

        case _:  # The user entered an invalid input.
            print("Invalid input!\nDon't do that! The wolf is coming!\n")
            choose_option(alarm_time, clock_format, False)  # Come back to choice of menu options.


def clock():
    """
    Clock main function.
    :return: ∅
    """
    try:
        clock_format_default = 24  # Clock format is set in 24h at the start of the program.
        alarm_default = None  # Alarm is turned off at the start of the program.

        print("\nWelcome to Grandma's clock!\n")
        print("In this menu, you can choose between different options:")

        choose_option(alarm_default, clock_format_default)  # Run the menu.

    except KeyboardInterrupt:  # Rerun the program from the beginning when KeyboardInterrupt is used.
        cls()
        clock()


if __name__ == "__main__":  # The program will be run only if executed directly, not if it called from another program.
    clock()
