
INCHES_IN_FOOT: int = 12

def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_IN_FOOT
    print(f"That is {inches} inches! in {feet} feet.")


if __name__ == '__main__':
    main()