import random

def coin_game():
    return random.choice(["Heads", "Tails"])

def coin_game():
    points=10

    while points>0:
        print("Current points: " +points)
        bet=int(input("How many points would you like to bet?"))
        if(bet==0):
            break
        if (bet<0) or (bet>points):
            print("Invalid Bet")
        else:
            guess=input("Will the coin flip Heads or Tails")
            if (guess != "H") or (guess !="T"):
                print("Invalid Guess")
            else:
                print("You were wrong, the coin flipped " )