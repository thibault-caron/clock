from datetime import timedelta, datetime
import datetime
import time

# function to add a second to a time
def clock_heart(H, M, S):
    clock = datetime.datetime(1, 1, 1, H, M, S)
    while True:
        clock = clock + datetime.timedelta(seconds=1)
        print(clock.time(), end="\r")
        #faire une variable a partir de stamp.time!!! 
        # et enlever le print!!!!
        # et prévoir une variablle start qui prend soi lheure locale, soi l'heure réglée 
        time.sleep(1)
        
clock_heart(16, 3, 00)



