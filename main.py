'''
Perfect Guess Game-This is a fun Number Guessing Game where the computer secretly selects a random number within a given range (for example, 1 to 100). 
Your task is to guess the number correctly. After each guess, the computer will give you hints such as “too high” or “too low” to guide you toward the answer.
Your luck rating will be calculated based on:How many attempts you take to guess the correct number.The amount of time you spend before finding it.
The faster and fewer tries you use, the luckier you are!
'''
import random
n=random.randint(1,100)

print("Welcome to the Game")
start=input("Press S to start the game or press Q to quit the game:")
while(start.lower() not in ["s", "q"]):
    print("Invalid Entry")
    start=input("Press S to start the game or press Q to quit the game:")
    
if(start.lower()=="q"):
    print("Thank you for playing!!!")
    exit()   
a=-1
guesses=1
while(a!=n) and (start.lower()=="s") and (start.lower()!="q"):
    a=(input("Guess the number(or press Q to quit):"))
    if(a.lower()=="q"):
        print("Thank you for playing!!!")
        exit()
    elif not a.isdigit():  
        print("Please enter a valid number!")
        continue
    
    num=int(a)
   
    if(num>100):
        print("Enter the number less than 100.")
    elif(num>n):
        print("Lower the number")
        guesses+=1
    elif(num<n):
        print("Higher the number")
        guesses+=1
    elif(num==n):
        print(f"Yayyy!!!You found {n} succesfully in {guesses} guesses.")
        break
    elif(guesses==1):
       print(f"Yayyy!!!You found {n} succesfully in first guess.")
       break
    elif(guesses<1):
        print("Thank you!!!")
        break
    
    
        
if(guesses<2):
    print("GOD LEVEL LUCK")
elif(guesses>=2 and guesses<=3):
    print("GRANDMASTER LEVEL LUCK")
elif(guesses>3 and guesses<=5):
    print("ACE LEVEL LUCK")
elif(guesses>5 and guesses<=10):
    print("PRO LEVEL LUCK")
elif(guesses>10):
    print("BEGINNER LEVEL LUCK")



