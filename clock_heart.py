
import time

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

# def display_time(choice):

#     test = False
#     while not test:
#         try:
#             choice = int(input("Finally, do you want 12 hours or 24 hours display ? (enter 12 or 24)",))
#             if choice == 12 or choice == 24:
#                 test = True
#             else:
#                 print("Your input must be 12 or 24.")
#         except ValueError:
#             print("Your input must be 12 or 24.")




def clock_heart(start_clock, dring_clock):
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
        alarm(dring_clock, clock)
        print_time(clock)

        s += 1
        time.sleep(1)



def print_time(tp=()):
    print(f"\r{tp[0]:02}:{tp[1]:02}:{tp[2]:02}", end="")

#pour une base 12, a 12:00 on change AM pou PM et on repart à 00:00 (après 12:00 on passe à 01:00)


def alarm(dring_clock, clock):
    if dring_clock[0] == clock[0] and dring_clock[1] == clock[1] and dring_clock[2] == clock[2]:
        cls()
        print(f"\rDRING DRING DRING\n")
        

def cls():
    """
    Clear the console on Windows or Linux OS.
    :return: ∅
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# def exit()1


def clock():
    """
    Clock main function.
    :return: ∅
    """

    # clean terminal screen
    cls()

    # print a welcome screen to set the clock
    print("Grandma's clock !\n")
    print("First, let's set the clock :")
    start_clock = clock_input()

    # clean terminal screen
    cls()

    # print a screen to set the alarm
    print("Then, let's set an alarm :")
    dring_clock = clock_input()

    # clean terminal screen
    cls()

    # print a screen to choose the display time
    #XXXXXXXXXXXXX

    print(f"The alarm is setted for {dring_clock[0]:02}:{dring_clock[1]:02}:{dring_clock[2]:02}\n")
    # clock = clock_heart(Clock[0], Clock[1], Clock[2],dring_clock)
    clock_heart(start_clock, dring_clock)
    # return clock, dring_clock



if __name__ == "__main__":
    clock()


