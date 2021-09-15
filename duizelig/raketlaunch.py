import time

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("LAUNCH!!")

seconds = 30
countdown(seconds)