# UNE COSC110 - Programming Task 1

Welcome to the Codetown Grocery Store Self-Check-In System! This Python script allows users to perform self-check-in at the grocery store, register items, apply discount cards, and compute the total cost of their purchases.

## Description

**STORE ITEMS**

Codetown's grocery store is a small establishment offering a limited selection of just four items:

**1. Apples:** priced at $5 per kilo

**2. Bananas:** priced at $3 per kilo

**3. Meat:** priced at $20 per kilo

**4. Fish:** priced at $17 per kilo

Customers have the flexibility to purchase any quantity of these items, and they can record their selections at the self-check-in register in any sequence.

**DISCOUNT CARDS**

Customers have the option to hold one or more discount cards, with three distinct types available:

**Pensioner Card:** This card extends a 10% discount to pensioner customers on all the purchased items.

**Weekend Card:** Geared toward weekend shopping, the Weekend Card provides a 7.5% discount on all purchased items when used during the weekend, specifically on Saturday or Sunday.

**Green Card:** Designed to promote a vegan lifestyle, the Green Card offers a 15% discount on apples and bananas. However, it comes with a trade-off as it adds a surcharge fee of 5% for both meat and fish.

In the event that a customer possesses more than one of the aforementioned cards, the discounts or surcharge are applied in the following order: first, the discount of the pensioner card is applied, followed by the discount of the weekend card (if applicable given the entered day of the week), and finally the discount or surcharge of the green card (depending on the item purchased).
## Getting Started

To use the Codetown's self-check-in system, follow these steps:

**1. Password Entry:**
Enter the correct password to open the self-check-in register.
The password 'Codetown' is case sensitive, the program will prompt the user to re-attempt the password entry until successful. 

**2. Day of the Week:**
Input the current day of the week when prompted, note that the day validation input is case-insensitive. This is required for applying certain discounts. For example, the Green Card discount will only be applied if the user enters the day as Saturday or Sunday. 

**3. Adding Discount Cards:**
Choose option 1 from the Registration Menu to add a discount card if applicable. The system supports Pensioner, Weekend, and Green cards. Discount cards can only be applied once during the program in the following order: Pensioner, Weekend and lastly Green cards.

**4. Registering Items:**
Choose option 2 from the Registration Menu to register a new item and follow the prompts to enter the type of item and its weight.

**5.Compute Total and Pay:**
Once all items are registered and the entered discount cards are applied, choose the option to compute the total cost. You will be prompted to press 'Enter' to complete the payment process.

**6. Closing the System:**
To close the self-check-in register, enter the password when prompted. The password 'Codetown' is case sensitive, the program will prompt the user to re-attempt the password entry until successful. 


## Usage Instructions

Run the script using a Python interpreter (I.e. Python 3.12.1)

```python
python cashier.py
```
Follow the on-screen prompts to navigate through the self-check-in process and ensure you enter the correct password for both opening and closing the self check-in system.
## Description

**STORE ITEMS**

Codetown's grocery store is a small establishment offering a limited selection of just four items:

**1. Apples:** priced at $5 per kilo

**2. Bananas:** priced at $3 per kilo

**3. Meat:** priced at $20 per kilo

**4. Fish:** priced at $17 per kilo

Customers have the flexibility to purchase any quantity of these items, and they can record their selections at the self-check-in register in any sequence.

**DISCOUNT CARDS**

Customers have the option to hold one or more discount cards, with three distinct types available:

**Pensioner Card** This card extends a 10% discount to pensioner customers on all the purchased items.

**Weekend Card:** Geared toward weekend shopping, the Weekend Card provides a 7.5% discount on all purchased items when used during the weekend, specifically on Saturday or Sunday.

**Green Card:** Designed to promote a vegan lifestyle, the Green Card offers a 15% discount on apples and bananas. However, it comes with a trade-off as it adds a surcharge fee of 5% for both meat and fish.

In the event that a customer possesses more than one of the aforementioned cards, the discounts or surcharge are applied in the following order: first, the discount of the pensioner card is applied, followed by the discount of the weekend card (if applicable given the entered day of the week), and finally the discount or surcharge of the green card (depending on the item purchased).
## Important Note

This Python script is only intended to be used for educational purposes and may require further enhancements for production use.
