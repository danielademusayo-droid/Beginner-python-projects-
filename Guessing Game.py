import random

# This picks a random number between 1 and 100
secret_number = random.randint(1, 100) 

guess = 0
guess_count = 0

#Hint for the user
while True:
    user_input = input("Take a guess between 1 and 100: ")
    
    # 2. Try to convert it to a number
    try:
        guess = int(user_input)
    except ValueError:
        # If the user entered a letter or symbol, print this
        print("Invalid input! Please type a regular number, not letters or symbols.")
        continue # Restart the loop to ask them again
    guess_count += 1
    
    # To restrict the user input 
    if guess not in range(1, 101):
	    print(f"{guess} is not valid") 
	    print("Pick between the range of 1 to 100")
	    continue #  Skip everything below and restart the loop.
           
    # Check if they won INSIDE the loop
    if guess == secret_number:
        print("Hurray🎉, You just got it right!!")
        break  # This stops the loop completely
    
    if guess < secret_number:
        print("HINT: Too low! keep guessing")
    elif guess > secret_number:
        print("HINT: Too high! Keep guessing")

#To count the number of guesses
if guess_count <= 5:
   print(f"It took just {guess_count} attempts")
   print("You are such a genius!!")
elif guess_count > 5:
   print(f"It took just {guess_count} attempts")
   print("That's a while, keep trying!!")
   

  
