temp = float(input("Enter your temperature: "))
unit = input("Farenheit or celsius (F of C): ")

if unit == "C": 
   temp = round((9 * temp) / 5 + 32, 1)
   print(f"Your tempetature in farenheit is: {temp}°F")
elif unit == "F":
   temp = round((temp - 32) * 5 / 9, 1)
   print(f"Your tempetature in Celsius is: {temp}°C")
else :
    print(f"{unit} is not valid")
   