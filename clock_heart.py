
import time


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
    print(tp)


def clock_input(clock=()):
    """
    Function used to set the clock.
    :return: return h, m, s
    """
    test = False
    while not test:
        try:
            clock=((int(input("Set the clock!\n\nFirst, choose hours : ", ))), (int(input("Next, choose minutes : ", ))), (int(input("And at the end, choose seconds : ", ))))
            if 0 <= clock[0] < 24:
                if 0 <= clock[1] < 60:
                    if 0 <= clock[2] < 60:
                        # print(H, M, S)
                        return clock
                    else:
                        print("Seconds has to be in a correct range!")
                else:
                    print("Minutes has to be in a correct range!")
            else:
                print("Hour has to be in a correct range!")
        except ValueError:
            print("What have you done?\nUse only integers numbers!\nGrandma has been eaten by a wolf!!\n")

def alarm(h, m, s, clock):
    if h == clock[0] and m == clock[1] and s == clock[2]:
        print("DRING")


dring_clock = clock_input()
CLOCK = clock_input()
clock = clock_heart(CLOCK[0], CLOCK[1], CLOCK[2])


