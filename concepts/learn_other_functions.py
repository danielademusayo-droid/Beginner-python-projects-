name = input("Enter your full name: ")
age = int(input("Enter your age: "))	

result = len(name)
result =  name.find("'d")

print("You are anAdult" if age >= 18  else "You are a child")

print(result)
#print(help(str)) to check other functiin that i might need
