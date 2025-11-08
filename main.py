print("Welcome to Pizza_pizza!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese? y or y: ")

def calculate_pizza_price():
    bill = 0
    if size == "S".lower():
        bill += 15
    elif size == "M".lower():
        bill += 20
    elif size == "L".lower():
        bill += 25
    else:
        print("You have chosen an invalid size.")

    if pepperoni == "Y".lower():
        if size == "S".lower():
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y".lower():
        bill += 1

    print(f"Your final bill is: ${bill}.")
calculate_pizza_price()
