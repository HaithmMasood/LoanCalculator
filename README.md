# Python Loan Calculator

A versatile loan calculator built in Python that can calculate annuity and differentiated payments, determine the overall loan duration, monthly payment amounts, and provide a comprehensive repayment schedule.

## Features

- Calculate the total number of monthly payments.
- Determine monthly payment amounts for annuity payments.
- Compute loan principal from annuity payments.
- Calculate differentiated payments for each month.
- Command-line interface for ease of use.
- Validation of input parameters with helpful error messages.

## How to Use

Run the script with the required command-line arguments:

- `--type`: Type of payment (`annuity` or `diff`).
- `--principal`: The principal amount of the loan.
- `--periods`: Number of months needed to repay the loan.
- `--interest`: The annual interest rate (as a percentage).
- `--payment`: The monthly payment amount (not required for `diff` type).

## Requirements

- Python 3.x

## Setup and Installation

1. Clone the repository or download the source code.
2. Run the script from the command line, providing the necessary parameters.

## Contributions

Contributions are welcome. Please fork the project and submit a pull request with your updates.

### Example Commands

```shell
# Calculate annuity payment
python CreditCalc.py --type=annuity --principal=500000 --periods=120 --interest=5.5

# Calculate differentiated payments
python CreditCalc.py --type=diff --principal=500000 --periods=120 --interest=5.5
