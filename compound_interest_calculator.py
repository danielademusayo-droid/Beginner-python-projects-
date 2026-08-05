# python compound interest calculator

principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter your principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break
        
while True:
    rate = float(input("Enter your interest rate: "))
    if rate < 0:
        print("rate can't be less than zero")
    else:
        break
        
        
while True:
    time = int(input("Enter your time in years: "))
    if time < 0:
        print("time can't be less than  zero")
    else:
        break
        
        
total = principle * pow(1 + rate / 100, time)
print(f"The compound interest is ${total: .2f}")
