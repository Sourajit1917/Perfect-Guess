'''
Perfect Guess Game-This is a fun Number Guessing Game where the computer secretly selects a random number within a given range (for example, 1 to 100). 
Your task is to guess the number correctly. After each guess, the computer will give you hints such as "too high" or "too low" to guide you toward the answer.
Your luck rating will be calculated based on:How many attempts you take to guess the correct number.The amount of time you spend before finding it.
The faster and fewer tries you use, the luckier you are!
'''
import random

# Main game loop - automatically restarts after each game
while True:
    print("\n" + "="*40)
    print("Welcome to the Number Guessing Game!")
    print("="*40)
    
    n = random.randint(1, 100)
    
    start = input("Press S to start the game, Q to quit this round, or EXIT to quit completely: ")
    while start.lower() not in ["s", "q", "exit"]:
        print("Invalid Entry")
        start = input("Press S to start the game, Q to quit this round, or EXIT to quit completely: ")
    
    if start.lower() == "exit":
        print("Thank you for playing! Goodbye!")
        break
        
    if start.lower() == "q":
        print("Thank you for playing this round!")
        continue  # Go back to start of main loop
    
    # Game logic
    a = -1
    guesses = 1
    
    while a != n and start.lower() == "s":
        a = input("Guess the number (1-100) or press Q to quit this round: ")
        if a.lower() == "q":
            print("Thank you for playing this round!")
            break
        elif not a.isdigit():  
            print("Please enter a valid number!")
            continue
        
        num = int(a)
       
        if num > 100:
            print("Enter a number less than or equal to 100.")
        elif num > n:
            print("Lower the number")
            guesses += 1
        elif num < n:
            print("Higher the number")
            guesses += 1
        elif num == n:
            if guesses == 1:
                print(f"Yayyy!!! You found {n} successfully in your first guess!")
            else:
                print(f"Yayyy!!! You found {n} successfully in {guesses} guesses.")
            
            # Display luck rating
            if guesses < 2:
                print("🌟 GOD LEVEL LUCK 🌟")
            elif guesses >= 2 and guesses <= 3:
                print("⭐ GRANDMASTER LEVEL LUCK ⭐")
            elif guesses > 3 and guesses <= 5:
                print("✨ ACE LEVEL LUCK ✨")
            elif guesses > 5 and guesses <= 10:
                print("💫 PRO LEVEL LUCK 💫")
            elif guesses > 10:
                print("🔥 BEGINNER LEVEL LUCK 🔥")
            break
