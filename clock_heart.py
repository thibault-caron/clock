
import time

def clock_heart():
    H = 23
    M = 59
    S = 57
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
        S += 1
        clock = (H, M, S)
        # print(clock)
        time.sleep(1)



clock_heart()


