from Temperature import celcius_to_kelvin
from Temperature import celcius_to_fahrenheit
from Temperature import fahrenheit_to_celcius

def main():
    while True:
        print("₹1. Celcius to Kelvin")
        print("2. Celcius to Fahrenheit")
        print("3. Fahrenheit to Celcius")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Kelvin: ", celcius_to_kelvin.convert(celcius))
        elif choice == 2:
            celcius = float(input("Enter temperature in Celcius: "))
            print("Temperature in Fahrenheit: ", celcius_to_fahrenheit.convert(celcius))
        elif choice == 3:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in Celcius: ", fahrenheit_to_celcius.convert(fahrenheit))
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()