# Logical operators
#or,and ,not

temp = 36
is_sunny = True

if 25 >= temp <= 32  and is_sunny:
	print("It is warm outside")
	print("It is sunny")
elif temp < 10 and not is_sunny:
	print("It is cold outside")
	print("It is cloudy")
elif temp > 32 and is_sunny:
	print("It is hot outside")
	print("It is sunny")
