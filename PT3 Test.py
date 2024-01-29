import tkinter as tk
from tkinter import messagebox

#Global list to store payment details
payments = []

#Global variable to track the operator window
operator_window = None

def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_credit_card(P):
    #Allow only numeric characters and limit to 16 digits
    return P.isdigit() and len(P) <= 16

def format_credit_card(credit_card):
    #Format credit card number with hyphens at every fourth digit
    return '-'.join(credit_card[i:i+4] for i in range(0, len(credit_card), 4))

def pay():
    #Get values from input fields
    amount_due_str = amount_due_var.get()
    credit_card_str = credit_card_var.get()

    #Validate input values
    if is_valid_float(amount_due_str) and is_valid_int(credit_card_str) and len(credit_card_str) == 16:
        amount_due = float(amount_due_str)

        #Check if the amount due is non-negative
        if amount_due >= 0:
            credit_card = int(credit_card_str)

            #Record payment details in a dictionary
            payment_details = {'Amount Due': amount_due, 'Credit Card Number': credit_card}

            #Append the dictionary to the global list
            payments.append(payment_details)

            #Show confirmation message box
            messagebox.showinfo("Payment Successful", f"Thank you for your payment of ${amount_due}.")

            #Reset the main interface to its default state
            amount_due_var.set("")
            credit_card_var.set("")
        else:
            #Display error message box for negative amount
            messagebox.showerror("Error", "Please enter a non-negative amount.")
            clear()
    else:
        #Display error message box for incorrect values
        messagebox.showerror("Error", "Please enter a valid amount and a 16-digit credit card number without spaces or other characters.")
        clear()
        
def clear():
    #Clear all input fields to defauly empty state
    amount_due_var.set("")
    credit_card_var.set("")

def operator_mode():
    global operator_window

    #Check if the operator window is already open, to avoid opening the same window again whenever the 'Operator Mode' button is clicked
    if operator_window is not None:
        operator_window.destroy()

    #Open new top-level window if Operator Mode is succeffully accessed
    operator_window = tk.Toplevel(root)
    operator_window.title("Operator Mode")
    operator_window.configure(bg="white")
    operator_window.geometry("200x100")

    #Centre contents vertically using columnconfigure
    operator_window.columnconfigure(0, weight=1)  #Adjust weight to center vertically

    #Widgets created for the operator window
    password_label = tk.Label(operator_window, text="Enter Password:")
    password_entry = tk.Entry(operator_window, show="*", bg="white")  #ensure password entry is concealed and display as asterisks "*****"
    submit_button = tk.Button(operator_window, text="Submit", command=lambda: check_password(operator_window, password_entry.get(), password_entry), bg="blue", fg="white")  # Set button color to blue

    password_label.grid(row=0, column=0, pady=5)
    password_entry.grid(row=1, column=0, pady=5)
    submit_button.grid(row=2, column=0, pady=5)


def check_password(operator_window, entered_password, password_entry):
    if entered_password == "Codetown":
        operator_window.destroy()  #Close the password window if operator mode password succesffully entered
        display_transactions()
    else:
        messagebox.showerror("Error", "Incorrect password. Please try again.")
        password_entry.delete(0, tk.END)  #Clear the password entry field to reattempt password entry


#Open a new window if operator mode password is entered successfully
def display_transactions():
    transactions_window = tk.Toplevel(root)#New top-level window to display transaction history
    transactions_window.title("Transactions")
    transactions_window.configure(bg="white")  

    #Display headings with bold text
    tk.Label(transactions_window, text="Amount:", font=('calibre', 10, 'bold'), bg="white").grid(row=0, column=0, pady=5, sticky="w")
    tk.Label(transactions_window, text="Credit Card:", font=('calibre', 10, 'bold'), bg="white").grid(row=0, column=1, pady=5, sticky="w")
   
    #Display transactions in the new window
    for index, transaction in enumerate(payments, start=1):
        formatted_credit_card = format_credit_card(str(transaction['Credit Card Number']))

        tk.Label(transactions_window, text=f"${transaction['Amount Due']}", font=('calibre', 10), bg="white").grid(row=index, column=0, pady=5, sticky="w")
        tk.Label(transactions_window, text=formatted_credit_card, font=('calibre', 10), bg="white").grid(row=index, column=1, pady=5, sticky="w")

    #Calculate and display total payments
    total_payments = sum(transaction['Amount Due'] for transaction in payments)
    tk.Label(transactions_window, text="Total Payments:", font=('calibre', 10, 'bold'), bg="white").grid(row=len(payments) + 1, column=0, pady=5, sticky="w")
    tk.Label(transactions_window, text=f"${total_payments}", font=('calibre', 10), bg="white").grid(row=len(payments) + 1, column=1, pady=5, sticky="w")

#Main
root = tk.Tk()

root.geometry("300x250")  #set window size
root.title("Codetown Grocery Store Self Check-In System")
root.configure(bg="white")  #Set background color to white

#Declare variables for storing amount due and credit card number
amount_due_var = tk.StringVar()
credit_card_var = tk.StringVar()

#Amount due label and input field
amount_due_label = tk.Label(root, text='Amount Due:', font=('calibre', 10, 'bold'), bg="white")  # Set background color to white
amount_due_entry = tk.Entry(root, textvariable=amount_due_var, font=('calibre', 10, 'normal'))

#Credit card label and input field
credit_card_label = tk.Label(root, text='Credit Card:', font=('calibre', 10, 'bold'), bg="white")  # Set background color to white
credit_card_entry = tk.Entry(root, textvariable=credit_card_var, font=('calibre', 10, 'normal'), show='*', validate='key', bg="white")  # Set background color to white
credit_card_entry['validatecommand'] = (root.register(validate_credit_card), '%P')

#Main window buttons
pay_button = tk.Button(root, text='Pay', command=pay, bg="blue", fg="white", font=('calibre', 10, 'bold'))  # Set button color to blue, make it bold
clear_button = tk.Button(root, text='Clear All', command=clear, bg="blue", fg="white", font=('calibre', 10, 'bold'))  # Set button color to blue, make it bold
operator_mode_button = tk.Button(root, text='Operator Mode', command=operator_mode, bg="dark red", fg="white", font=('calibre', 10, 'bold'))  # Set button color to blue, make it bold

#Place widgets in main window using grid method
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

amount_due_label.grid(row=5, column=0, pady=10, padx=10, sticky="w")
amount_due_entry.grid(row=5, column=1, pady=10, padx=10, sticky="ew", columnspan=2)  # Adjusted sticky and added columnspan
credit_card_label.grid(row=6, column=0, pady=10, padx=10, sticky="w")
credit_card_entry.grid(row=6, column=1, pady=10, padx=10, sticky="ew", columnspan=1)  # Adjusted sticky and added columnspan
pay_button.grid(row=7, column=1, pady=10, padx=10, sticky="ew", columnspan=1)  # Adjusted sticky and added columnspan
clear_button.grid(row=8, column=1, pady=10, padx=10, sticky="ew", columnspan=1)  # Adjusted sticky and added columnspan
operator_mode_button.grid(row=9, column=1, pady=10, padx=10, sticky="ew", columnspan=1)  # Adjusted sticky and added columnspan

#Tkintr event loop
root.mainloop()
