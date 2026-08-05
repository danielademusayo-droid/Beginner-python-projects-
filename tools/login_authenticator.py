print("======Welcome to futa coding club====\n")

#user information
Username = input("Enter your username; ")
password = input("Enter a password: ")
confirm_password = input("Confirm your password: ")
age = int(input("Enter your age:"))

#input Validation
if password == confirm_password and age >= 18:
	print("Account created successfully")
	print(f"{Username}, welcome to Futa coding club!!")
elif password != confirm_password:
	print("Password does not match")
elif age >= 13 and age < 18:
	print("You have joined the junior section, Welcome ")
elif age < 13:
	print("You are too young to join.")
else:
	print("Invalid input!!!")
