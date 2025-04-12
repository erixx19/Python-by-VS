def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    print("Welcome, let us see how Temp. changes its color based on scale!")
    
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the suspected unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

        if unit == "C":
            print(f"\n{value}°C is equal to:")
            print(f"{celsius_to_fahrenheit(value):.2f}°F")
            print(f"{celsius_to_kelvin(value):.2f}K")
        elif unit == "F":
            print(f"\n{value}°F is equal to:")
            print(f"{fahrenheit_to_celsius(value):.2f}°C")
            print(f"{fahrenheit_to_kelvin(value):.2f}K")
        elif unit == "K":
            print(f"\n{value}K is equal to:")
            print(f"{kelvin_to_celsius(value):.2f}°C")
            print(f"{kelvin_to_fahrenheit(value):.2f}°F")
        else:
            print("Invalid unit entered. Please use C, F, or K.")
    
    except ValueError:
        print("Invalid input! Please enter a numeric temperature value.")

if __name__ == "__main__":
    main()
