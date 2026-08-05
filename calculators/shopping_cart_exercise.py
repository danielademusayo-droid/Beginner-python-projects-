# Shopping cart program
item = input("What item would you like to buy?: ")
price = float(input("How much is it?: "))
quantity = int(input("How many will you like to buy?: "))
Total = price * quantity

print(f"You have bought {quantity} {item}s")
print(f"Your total is: ${Total}")
