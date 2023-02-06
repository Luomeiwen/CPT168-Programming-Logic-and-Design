#!/usr/bin/env python3
# Meiwen Luo, February 5, 2023, CPT168-W32, Lab04-1
# This programmar is to define get_float and get_int functions.
        

def get_float(prompt, low_validity, high_validity):
    value = float(input(prompt))
    # Keep input until value is valid.
    while True:
        # Judge if value is valid.
        if value > low_validity and value <= high_validity:
            return value 
        # Output error message.
        else:
            print(f"This value need to be greater than {low_validity} and lower or equal to {high_validity}.")
            value = float(input(prompt))

def get_int(prompt, low_validity, high_validity):
    value = int(input(prompt))
    # Keep input until value is valid.
    while True:
        # Judge if value is valid.
        if value > low_validity and value <= high_validity:
            return value 
        # Output error message.    
        else:
            print(f"This value need to be greater than {low_validity} and lower or equal to {high_validity}.")
            value = int(input(prompt))

def main():
    choice = "y"
    # Test multiple times.
    while choice.lower() == "y":
        a = get_float("Input a value ", 1, 10)
        print(a)
        b = get_int("Input a value ", 1, 10)
        print(b)
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
