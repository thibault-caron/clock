
import time
import datetime

def clock_input(clock=()):
    """
    Function used to set the clock.
    :return: A tuple of hours, minutes and seconds user has chose.
    """
    test1 = False
    test2 = False
    test3 = False
    while not test1:
        try:
            hours = int(input("\nFirst, choose hours : ", ))
            if 0 <= hours < 24:
                test1 = True
            else:
                print("\nHour has to be in a correct range!")
        except ValueError:
            print("\nWhat have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test2:
        try:
            minutes = int(input("Next, choose minutes : ", ))
            if 0 <= minutes < 60:
                test2 = True
            else:
                print("\nMinutes has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    while not test3:
        try:
            seconds = int(input("And at the end, choose seconds : ", ))
            if 0 <= seconds < 60:
                test3 = True
            else:
                print("\nSeconds has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\n\nGrandma has been eaten by a wolf!!\n")

    clock = (hours, minutes, seconds)
    return clock


# def clock_now(clock=()):
#     """
#     Function used to return computer time.
#     :return: A tuple of hours, minutes and seconds.
#     """
#     hours = datetime.datetime.now().hour
#     minutes = datetime.datetime.now().minute
#     seconds = datetime.datetime.now().second
#     clock =(hours, minutes, seconds)
#     return clock


def clock_heart(H, M, S):
    # loop for add a second and return a time
    while True:

        if S == 60 :
            S = 0
            M += 1
            if M == 60 :
                M = 0
                H += 1
                if H == 24 :
                    H = 0
        clock = (H, M, S)
        alarm(dring_clock[0], dring_clock[1], dring_clock[2], clock)
        print_time(clock)
        S += 1
        time.sleep(1)

def print_time(tp=()):
    print(f"\r{tp[0]:02}:{tp[1]:02}:{tp[2]:02}", end="")

def alarm(h, m, s, clock):
    if h == clock[0] and m == clock[1] and s == clock[2]:
        print("DRING")

# def display_menu():
#     """
#     Display the menu on the terminal.
#     :return: ∅
#     """
#     print("\nWelcome to Grandma's clock!\n")

#     print("In this menu, you can choose between different options:\n")

#     print("1: Display current local time")
#     print("2: Set the time you want")
#     print("3: Set an alarm")
#     print("4: Switch between 12 hours and 24 hours display")
#     print("5: Pause your clock")
#     print("6: Exit\n")

# def choose_option(alarm_time):
#     """
#     Take and execute the function the user wants.
#     :return: ∅
#     """
#     menu_option = input("Choose your option (enter '1' to '6'): ")

#     match menu_option:
#         case "1":
#             computer_time = clock_now()
#             display_time(alarm_time, computer_time)
#         case "2":
#             print("\nSet the clock!")
#             user_time = clock_input()
#             display_time(alarm_time, user_time)
#         case "3":
#             print("\nSet the alarm!")
#             alarm_tuple = clock_input()
#             alarm_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month,
#                                            datetime.datetime.now().day, alarm_tuple[0], alarm_tuple[1], alarm_tuple[2])
#             display_menu()
#             choose_option(alarm_time)
#         case "4":
#             print("\nHour format switched!")
#             display_menu()
#             choose_option(alarm_time)
#         case "5":
#             print("\nClock paused")
#             display_menu()
#             choose_option(alarm_time)
#         case "6":
#             cls()
#             exit()
#         case _:
#             print("Invalid input!\nDon't do that! The wolf it's coming!")
#             choose_option(alarm_time)


# def clock():
#     """
#     Clock main function.
#     :return: ∅
#     """
#     try:
#         alarm_default = None
#         display_menu()
#         choose_option(alarm_default)
#     except KeyboardInterrupt:
#         cls()
#         clock()



dring_clock = clock_input()
CLOCK = clock_input()
clock = clock_heart(CLOCK[0], CLOCK[1], CLOCK[2])

