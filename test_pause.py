from time import sleep
from datetime import datetime, timedelta
from os import system, name
import keyboard


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
            print("\nWhat have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

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

def display_time(alarm, clock, hour_format):
    """
    Display the chosen time updated every second.
    When clock is set at None, display the current time.
    :param alarm: A datetime formatted alarm.
    :param clock: A tuple of hours, minutes and seconds.
    :param hour_format: Hour display format (24h or 12h with AM/PM).
    :return: ∅
    """
    global paused  # Access the global paused flag

    clock_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, clock[0], clock[1], clock[2])
    increment = timedelta(seconds=1)  # Create a one-second step to increment the time.
    print()  # Skip a line before displaying the clock for better visual comfort.

    while True:
        if keyboard.is_pressed('space'):  # Check if the space key is pressed
            paused = not paused  # Toggle the paused state
            print(f"\nClock {'paused' if paused else 'resumed'}!\n")
            sleep(0.5)  # Debounce the key press to avoid toggling multiple times in one press
        
        if paused:
            continue  # Skip the rest of the loop until resumed

        if hour_format == 24:
            print(f"\r{clock_time.strftime('%H:%M:%S')}", end="")  # Print time in 24h format (16:25:10).
        else:
            print(f"\r{clock_time.strftime('%I:%M:%S %p')}", end="")  # Print time in 12h format (04:25:10 PM).

        if alarm is not None:
            if alarm == clock_time:  # Checks if it is alarm time.
                print("\nWake up quick!!\nWolf is near your house!")

        clock_time = clock_time + increment
        sleep(1)  # Wait a second before updating the time

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
        print("\n1: Display current local time (use last, space to pause)")
        print("2: Set the time you want (use last, space to pause)")
        print("3: Set an alarm")
        print("4: Switch between 12 hours and 24 hours display")
        print("5: Exit\n")

    if view_menu is True:  # Check if the clock menu has to be displayed.
        display_menu()  # Display the clock menu.
    menu_option = input("Choose your option (enter '1' to '6'): ")

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
            choose_option(alarm_time, clock_format)  # Come back to the choice of menu options and display the menu again.
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

    paused = False # Global flag for pausing the clock
    
    clock()
