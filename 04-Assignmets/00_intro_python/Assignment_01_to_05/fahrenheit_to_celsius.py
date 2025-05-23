def main():
    fahrenheit = float(input("\033[1;3m Enter tempreture in Fahrenheit: \033[0m "))
    

    celcius: float = (fahrenheit - 32) * 5.0/9.0  # ye formula copy past kar ke rakha gaya hai

    print(f"tempreture in Fahrenheit {fahrenheit} = {celcius}C")

if __name__ == '__main__':
   main()    