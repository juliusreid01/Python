# used to measure time
import time
# used to generate random numbers
import random

def waiting_game():    
    target = random.randint(2,4)
    print("Your target is {} seconds".format(target))

    # get user input
    input(' ---Press Enter to Begin--- ')
    # performance counter clock
    start = time.perf_counter()

    input("\nPress Enter again after {} seconds ...".format(target))
    elapsed = time.perf_counter() - start

    print("\nElapsed time: {0:.3f} seconds".format(elapsed))
