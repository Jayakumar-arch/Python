'''1. Coffee Shop Ordering System (Basic)
Scenario:
You are developing a simple ordering system for a new coffee shop. The system needs to calculate the total bill for a customer's order and apply a discount if applicable. 
Task:
Create a Python program that performs the following actions:
Display a menu with item names and prices (e.g., Coffee: $3.50, Muffin: $2.00, Bagel: $4.00).
Prompt the user to select items and quantities.
Calculate the total cost of the order.
Apply a 10% discount if the total bill exceeds $20.00.
Display the final amount payable.'''


menu=["Coffee","Muffin","Bagel"]
print(menu)
user=input("Enter the menu:").lower()
quantities=int(input("Enter the quantities :"))
price=0
discount=0
if user=="coffee":
    price=3.50
    discount=10
    menu_name = "Coffee"
elif user=="muffin":
    price=2.00
    discount=10
    menu_name = "Muffin"
elif user=="bagel":
    price=4.00
    discount=10
    menu_name = "Bagel"
else:
    print("invalide menu")
print("- - - - - - - - - - - - - - - - - - - -")
print("Menu           :",user)
print("Quantities     :",quantities)
print("Price          :$",price)
print("Discount       :",discount,"%")
totalamount=price*quantities
print("Total Amount   : $", totalamount)
discount_amount = totalamount * (discount / 100)
print("Discount Amount: $", discount_amount)
final_amount = totalamount - discount_amount
print("Finalamount    : $",final_amount)
print("- - - - - - - - - - - - - -  - - - - - -")


'''2.Scenario: You are processing credit card numbers (e.g., "4532111188885678").
Task: Write a function that:
Takes the string as input.
Returns a "masked" version where all digits except the last 4 are replaced by * (e.g., "************5678").
Focus: Function definitions, string slicing, and the * repetition operator.'''


def credit(card_number):
    marked="*"*(len(card_number)-4)
    return marked+card_number[-4:]
card_number=("4532111188885678")
marked_card=credit(card_number)
print(marked_card)



    

