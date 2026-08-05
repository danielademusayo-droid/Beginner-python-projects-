print("---Basic Calculator---")
# Project to build my problem solving and critical thinking skills
num1= float(input("First Number: "))
num2= float(input("Second Number: "))
Operator = input("Enter the operator (+,-,*,/): ")

if Operator == "+":
	result = num1 + num2
elif Operator == "-":
	  result = num1 - num2
elif Operator == "*":
	  round(result = num1 * num2),2
elif Operator == "/":
	  result = num1 / num2  if num2 != 0 else "Cannot divide by zero!"
else: 
      result = "invalid operation!"
      
print(f"Result: {result}")


