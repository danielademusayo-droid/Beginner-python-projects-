Weight = float(input("Enter your weight: "))
unit =  input("Weight unit (kg or lbs): ")


if unit == "kg":
	Weight = Weight * 2.205
	unit = "lbs"
elif unit == "lbs":
	Weight = Weight / 2.205
	unit = "kg"
else :
   print(f"{unit} is not valid")
print(f"Your weight is : {round(Weight, 2)} {unit}.")
	