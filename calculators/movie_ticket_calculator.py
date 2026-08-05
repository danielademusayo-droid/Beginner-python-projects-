nickname = input("Enter your nickname: ")
base_price = 15
age = int(input("How old are  you?: "))
seat_type = input("Choose your seat type (Premium or Gold): ")
show_time = 'Evening'

if age > 17:
    print(f'{nickname}, you are eligible to book a ticket')

if age >= 21:
    print(f'{nickname}, you are eligible for Evening shows')
else:
    print(f'{nickname}, you are not eligible for Evening shows')

is_member = input("Are you a member? (True or False): ")
is_weekend = input("Are you coming on weekends? (True or False): ")

discount = 0
if is_member and age >= 21:
    discount = 3
    print(f'{nickname}, you are qualified for membership discount')
else:
    print(f'{nickname}, you are not qualified for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = extra_charges + service_charges + base_price - discount
    print("Final price of ticket:",final_price) 
else:
    print('Ticket booking failed due to restrictions')
