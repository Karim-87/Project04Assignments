import random

NUM_SIDES: int = 6

def main():

    #random.seed(1)
    
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    total: int = die1 + die2
    
    
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
