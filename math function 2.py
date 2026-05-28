import math 

#x = 25.4

#print(math.pi)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)
#print(result)
# Exercise 3 
#radius = float(input("What is the radius of the circle: "))
#Area =  math.pi * radius**2
#print(f" The Area of the circle is:  {round(Area, 2)}cm²")
a = float(input("What is the value of a: "))
b = float(input("What is the value of b: "))
#c = math.sqrt(a**2 + b**2) or ---->
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of the hypoteneus is: {round(c, 2)}cm")