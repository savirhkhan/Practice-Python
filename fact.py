
import time

run = input("Start?: ")
seconds = 0
if run is 'yes':
    while seconds != 10:
        print('>',seconds)
        time.sleep(1)
        seconds +=1

