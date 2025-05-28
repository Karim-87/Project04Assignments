def main():


    dividend: int = int(input("\033[1;3m Please enter an integer to be divided: \033[0m "))
    divisor: int = int(input("\033[1;3m Please enter an integer to divide by: \033[0m "))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


if __name__ == '__main__':
    main()
