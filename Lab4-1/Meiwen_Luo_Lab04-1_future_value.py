#!/usr/bin/env python3
# Meiwen Luo, February 5, 2023, CPT168-W32, Lab04-1
# This programmar is to enhance the future value.

from validation import get_float, get_int
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    # Calculate for each month.
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

# def get_float(prompt,low_validity, high_validity):
#     value = float(input(prompt))
#     while True:
#         if value > low_validity and value <= high_validity:
#             return value 
#         else:
#             print(f"This value need to be greater than {low_validity} and lower or equal to {high_validity}.")
#             value = float(input(prompt))

# def get_int(prompt,low_validity, high_validity):
#     value = int(input(prompt))
#     while True:
#         if value > low_validity and value <= high_validity:
#             return value 
#         else:
#             print(f"This value need to be greater than {low_validity} and lower or equal to {high_validity}.")
#             value = int(input(prompt))

def main():
    choice = "y"
    # Calculate multiple times.
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
