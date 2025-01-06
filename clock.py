"""
Authors : Lorenzo OTTAVIANI, Anna LEITE et Thibault CARON
Date : 06/01/2025 15h37
Aim of the program :
    Display the clock.
Input : clock :
Output :
"""

import time

try:
    clock_input = int(input("Set yours hours : ", )), int(input("yours minutes : ", )), int(input("yours seconds : ", ))
    print(clock_input)
except ValueError:
    print("Grandma has been eaten by a wolf!")

clock_in = 12, 25, 37
clock_sec = clock_in[0]*3600 + clock_in[1]*60 + clock_in[2]
clock_sec = clock_sec - 3600  # Correct time because it begins at 1:00 AM
while True:
    print("\r", time.strftime("%H:%M:%S", time.localtime(clock_sec)), end="")
    clock_sec += 1
    time.sleep(1)
