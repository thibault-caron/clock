
import time

def clock_input(clock=()):
    """
    Function used to input a time.
    :return: A tuple clock.
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


def clock_heart(start_clock, dring_clock, choice_print_time, choice_set_alarm):
    """
    Function that makes an infinite loop to create time whith incrementation.
    :return: print according to user's choices.
    """
    # loop for add a second and return a time
    h = start_clock[0]
    m = start_clock[1]
    s = start_clock[2]
    
    while True:
        if s == 60 :
            s = 0
            m += 1
            if m == 60 :
                m = 0
                h += 1
                if h == 24 :
                    h = 0
        clock = (h, m, s)

        if choice_set_alarm == 1 :
            alarm(dring_clock, clock)

        if choice_print_time == 1:
            print_time_24(clock)
        elif choice_print_time == 2:
            print_time_12(clock)

        s += 1
        time.sleep(1)



def print_time_24(tp=()):
    """
    Function used to input a time.
    :return: A tuple clock.
    """
    print(f"\r{tp[0]:02}:{tp[1]:02}:{tp[2]:02}", end="")

def print_time_12(tp=()):
    """
    Function used to input a time.
    :return: A tuple clock.
    """
    part = "AM"
    if tp[0] == 0:
        print(f"\r12:{tp[1]:02}:{tp[2]:02} {part}", end="")
    elif (1, 0, 0) <= tp < (12, 0, 0):
        print(f"\r{tp[0]:02}:{tp[1]:02}:{tp[2]:02} {part}", end="")
    elif tp[0] == 12:
        part = "PM"
        print(f"\r{tp[0]:02}:{tp[1]:02}:{tp[2]:02} {part}", end="")
    elif 13 <= tp[0] < 24:
        part = "PM"
        print(f"\r{(int(tp[0])-12):02}:{tp[1]:02}:{tp[2]:02} {part}", end="")



def alarm(dring_clock, clock):
    """
    Function used to input a time.
    :return: A tuple clock.
    """
    if dring_clock[0] == clock[0] and dring_clock[1] == clock[1] and dring_clock[2] == clock[2]:
        cls()
        print(f"\rDRING DRING DRING\n")

def binary_choice():
    """
    Translate a choice in integers 1 or 2.
    :return: Integer 1 or 2.
    """
    test = False
    while not test:
        try:
            binary = int(input("\nYour choice: ", ))
            if binary == 1 or binary == 2:
                return binary
            else:
                print("\nYou can only choose 1 or 2")
        except ValueError:
            print("\nUse only integers numbers")
        

def cls():
    """
    Clear the console on Windows or Linux OS.
    :return: ∅
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# def exit()1
# def stop-restart
# Trouver un moyen de faire disparaitre le message de l'alarme après n secondes


def clock():
    """
    Clock main function.
    :return: ∅
    """
    # variables initialization
    choice_print_time = None
    choice_set_alarm = None
    dring_clock = None


    # clean terminal screen
    cls()

    # print a welcome screen and give a first choice : the display's time
    print("Grandma's clock !\n")
    print("First, let's choose the display's time:")
    print("\n1: 24 display (00:00:00)")
    print("2: 12 display (00:00:00 AM/PM)")
    # choice_print_time is update with the user choice
    choice_print_time = binary_choice()

    # clean terminal screen
    cls()

    # print a screen to choose if you want to set the alarm
    print("Do you want to set an alarm ?")
    print("\n1: YES")
    print("2: NO")
    # choice_set_alarm is update with the user choice
    choice_set_alarm = binary_choice()

    # if the user choice is YES, a new screen to set the alarm
    if choice_set_alarm == 1:
        cls()
        print("Fine ! Let's set an alarm :")
        dring_clock = clock_input()
    
    # clean terminal screen
    cls()

    #  a screen to set the clock
    print("Then, let's set the clock !")
    start_clock = clock_input()

    # clean terminal screen
    cls()

    # Final screen with the alarm time reminder if the user choose it 
    # and the time display in the chosen format.
    if choice_set_alarm == 1:
        print(f"The alarm is setted for {dring_clock[0]:02}:{dring_clock[1]:02}:{dring_clock[2]:02}\n")

    # on lance l'horloge
    clock_heart(start_clock, dring_clock, choice_print_time, choice_set_alarm)


if __name__ == "__main__":
    clock()


