import random 

r_num = random.randrange(11)

while True:

    player_guess = int(input("Enter the number you want to guess: "))

    if player_guess == r_num :
        print(f" It was {r_num} congrats!!, You guessed it right")
        break
    
    else:
        print("You guessed it wrong.")

    

