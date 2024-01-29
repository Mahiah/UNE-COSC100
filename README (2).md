# UNE COSC110 - Programming Task 3

This program aims to enhance the existing automated self-check-in system by introducing a graphical user interface (GUI) for credit card payments. The current system has been well-received, but there have been complaints about the payment process, which requires customers to visit the service desk for transactions.

The new GUI will allow customers to make credit card payments seamlessly, eliminating the need for manual processing. This Readme provides an overview of the program's functionality, requirements, and usage instructions.
## Features

**Payment Processing**
- Users can enter the amount due for their grocery store transactions.
- Credit card information is required for payment.
- Payment validation ensures that the entered amount is - non-negative and that the credit card number is a 16-digit integer.

**Operator Mode**
- Authorized personnel can access an "Operator Mode" using a password.
- In "Operator Mode," personnel can view a summary of transactions, including the amount and credit card details.
- The system calculates and displays the total payments made.

## Getting Started

To view the desired maximum ratio, follow these steps:

**1. Run the Program:**

Use a Python 3 interpreter to run the following program:

    payments.py 

**2. Payment Process**
- Use the GUI to interact with the widgets.
- Enter the a positive numerical amount in the "Amount Due" field. Only positive floating-numbers can be inputted.
- Enter the 16-digit credit card number in the "Credit Card" field. Only positive integers can be inputted.
- Click the 'Clear All' button to clear all input fields.
- Click the "Pay" button to process the payment.
- Error handling has been included, where an error message will "pop up" in a new window if the amount due or credit card fields are entered incorrectly. Any letters, special symbols, or negative numbers will not be accepted and you will be prompted to re-enter a valid input.
- In this instance, all input fields will be reset to empty


**3. Operator Mode**

- Click the "Operator Mode" button to access the password-protected window.
- Enter the correct password ("Codetown") to view transaction details.
- Authorized personnel can view the history of the transaction details dislaying all payments, credit cards used for each payment and the total payment made.








 


## Key Functions

The code is organized into functions and utilizes the Tkinter library for creating the GUI. Key functions include payment processing, operator mode, password validation, and displaying transaction details.

**1. Payment Processing**

The payment-related functions ensure the accurate processing of user transactions:

`def pay():`

- Retrieves values from the input fields for the amount due and credit card information.
- Validates the input data, checking for a valid float for the amount and a valid 16-digit integer for the credit card.
- Ensures that the entered amount is non-negative.
- Records payment details in a dictionary and appends it to the global list of payments.
- Displays a confirmation message box for successful payments or error message boxes for invalid inputs.
- Resets the main interface to its default state after processing.

`def clear():`

- Clears the input fields, allowing users to reset the interface for a new transaction.

**2. Operator Mode**

`def operator_mode():` 

- Checks if the operator window is already open to avoid duplication.
- Creates a new window for operator mode, prompting the user to enter a password.
- Utilizes Tkinter's Toplevel widget to create a new window.
- Dynamically adjusts the window's size and contents to enhance user experience.

`def check_password():`

- Validates the entered password for operator mode.
- If the password is correct, it closes the password window and invokes display_transactions() to show transaction details.
- Displays an error message if the password is incorrect and clears the password entry field.

`def display_transactions():`

- Creates a new window to display transaction details.
- Utilizes Tkinter's Toplevel widget for a new window.
- Displays transaction headings and iterates over the global list of payments to present individual transactions.
- Calculates and displays the total payments made.

**3. input Validation and Formatting**

`def is_valid_float(value)` and `def is_valid_int(value):`

- Validate whether a given value can be converted to a float or integer, respectively.

`def validate_credit_card(P):`

- Validates credit card numbers, allowing only numeric characters and limiting the length to 16 digits.

`def format_credit_card(credit_card):`

- Formats a credit card number by adding hyphens at every fourth digit.

**4. GUI Setup**

- The code initializes the Tkinter GUI with labels, entry fields, and buttons.
- Utilizes the grid method to position widgets in a grid layout.

**5. Main Loop and Tkinter event loop**

- The code sets up the main Tkinter window, specifies its geometry, title, and background color.
- The mainloop() method runs the Tkinter event loop.
## Key Functions

The code is organized into functions and utilizes the Tkinter library for creating the GUI. Key functions include payment processing, operator mode, password validation, and displaying transaction details.

**1. Payment Processing**

The payment-related functions ensure the accurate processing of user transactions:

`def pay():`

- Retrieves values from the input fields for the amount due and credit card information.
- Validates the input data, checking for a valid float for the amount and a valid 16-digit integer for the credit card.
- Ensures that the entered amount is non-negative.
- Records payment details in a dictionary and appends it to the global list of payments.
- Displays a confirmation message box for successful payments or error message boxes for invalid inputs.
- Resets the main interface to its default state after processing.

`def clear():`

- Clears the input fields, allowing users to reset the interface for a new transaction.

**2. Operator Mode**

`def operator_mode():` 

- Checks if the operator window is already open to avoid duplication.
- Creates a new window for operator mode, prompting the user to enter a password.
- Utilizes Tkinter's Toplevel widget to create a new window.
- Dynamically adjusts the window's size and contents to enhance user experience.

`def check_password():`

- Validates the entered password for operator mode.
- If the password is correct, it closes the password window and invokes display_transactions() to show transaction details.
- Displays an error message if the password is incorrect and clears the password entry field.

`def display_transactions():`

- Creates a new window to display transaction details.
- Utilizes Tkinter's Toplevel widget for a new window.
- Displays transaction headings and iterates over the global list of payments to present individual transactions.
- Calculates and displays the total payments made.

**3. input Validation and Formatting**

`def is_valid_float(value)` and `def is_valid_int(value):`

- Validate whether a given value can be converted to a float or integer, respectively.

`def validate_credit_card(P):`

- Validates credit card numbers, allowing only numeric characters and limiting the length to 16 digits.

`def format_credit_card(credit_card):`

- Formats a credit card number by adding hyphens at every fourth digit.

**4. GUI Setup**

- The code initializes the Tkinter GUI with labels, entry fields, and buttons.
- Utilizes the grid method to position widgets in a grid layout.

**5. Main Loop and Tkinter event loop**

- The code sets up the main Tkinter window, specifies its geometry, title, and background color.
- The mainloop() method runs the Tkinter event loop.
## Important Note

This Python script is only intended to be used for educational purposes and may require further enhancements for production use.