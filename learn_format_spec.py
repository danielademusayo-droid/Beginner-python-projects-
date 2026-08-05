#format specifiers : Thay are used in f strings to format your strings
price1 = 2500.4567
price2 = -345.783
price3 = 1234.567

print(f"Price 1 is ${price1: ^+,.2f}")
print(f"Price 2 is ${price2: ^+,.2f}")
print(f"Price 3 is ${price3: ^+,.2f}")
# :, = comma seperator
# : = insert a space before positive number e.t.c
