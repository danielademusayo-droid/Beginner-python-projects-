# WHILE LOOP = execute some code WHILE some condition remains true
age = int(input("Enter your age: "))
 
while age < 0:
	print("Your age cannot be negative")
	age = int(input("Enter your age: "))

print(f"You are {age} years old")
