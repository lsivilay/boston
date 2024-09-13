transportation = 49.2
food = 180
activities = 264
merch = 150
min_amount = transportation + food + activities 

amount = float(input("Enter the amount of money you saved: "))

if amount >= min_amount:
    print(f"You have enough saved up!")
else: 
    print(f"You do not have enough saved up. You need to save ${min_amount-amount:,.2f} more.") 

additional = input("Do you plan on getting merch?: ")

if additional == "Yes":
    print(f"You need to save ${min_amount+merch:,.2f} total.")
elif additional == "yes":
    print(f"You need to save ${min_amount+merch:,.2f} total.")
elif additional == "yah":
    print(f"You need to save ${min_amount+merch:,.2f} total.")
else:
    print("You don't need to save anymore money!")