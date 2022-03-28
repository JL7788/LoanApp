# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!
total_num_of_loans = len(loan_costs)

print(total_num_of_loans)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

sum_of_loans = sum(loan_costs)

print(sum_of_loans)


# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!

average_loan_amount = sum_of_loans / total_num_of_loans

print(average_loan_amount)

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print(future_value, remaining_months)


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

present_value = [future_value / (1 + 0.2/12) ** remaining_months]


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if present_value >= loan_costs:
    print("The loan is worth at least the cost to buy it")
elif present_value < loan_costs:
    print("The loan is too expensive and not worth the price")




# Part 4
# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

price = new_loan["loan_price"]
future_value = new_loan["future_value"]
remaining_months = new_loan["remaining_months"]
annual_discount_rate = 0.20

def present_val_calc(future, remaining, annual_disc):
    presentval = [future / (1 + annual_disc / 12) ** remaining]
    return presentval

present_val_calc(future_value, remaining_months, annual_discount_rate)
print(f'The present value is ${presentval:.2f}')



# how do i round this?

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!





"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""




loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = [] 

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

for loan in loans:
    price = loan["loan_price"]
    if price <= 500:
        inexpensive_loans.append(loan)


# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

print(inexpensive_loans)


"""Part 5: Save the results.

# Output this list of inexpensive loans to a csv file
#     1. Use `with open` to open a new CSV file.
#         a. Create a `csvwriter` using the `csv` library.
#         b. Use the new csvwriter to write the header variable as the first row.
#         c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#             i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

#     Hint: Refer to the official documentation for the csv library.
#     https://docs.python.org/3/library/csv.html#writer-objects

"""


from pathlib import Path
import csv
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

with open(output_path, 'w', newline='') as csvfile:
    cswriter = csv.writer(csvfile)
    cswriter.writerow(header)
    for loan in inexpensive_loans:
        cswriter.writerow(loan.values()) 


# @TODO: Use the csv library and `csv.writer` to write the header row



# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!




