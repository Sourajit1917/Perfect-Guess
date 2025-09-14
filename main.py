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


