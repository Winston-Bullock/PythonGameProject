import random
def coin_flip():
    return random.choice(["Heads","Tails"])
    
#multi_flip(num) -> Flips a coin num times and returns the results
def multi_flip(num):

    #Data Decleration
    heads=0
    tails=0

    #While loops -> condition
    #For loops -> exact # of loops
    for x in range(num):
        flip=coin_flip()
        if(flip=="Heads"):
            heads=heads+1
        else:
            tails=tails+1

    print("You flipped "+str(heads)+" heads and "+str(tails)+" tails.")
    print("Percentage of Heads:"+str(100*heads/num)+"%")
    print("Percentage of Tails:"+str(100*tails/num)+"%")

    if(heads==tails):
        print("You flipped the same number pf heads and tails")
    elif(heads>tails):
        print("You flipped more heads than tails")
    elif(heads<tails):
        print("You flipped more tails than heads")

def predict():
    num_guesses=0
    while True:
        prediction=input("Do you think the coin will flip Heads or Tails")
        result=coin_flip()
        if(prediction==result):
            print("You were right! The coin flipped "+result)
            num_guesses=num_guesses+1
        else:
            print("You were wrong :(The coin flipped "+result)
            break
    print("You guesses right "+str(num_guesses)+" times")

def score(num):
    score=10
    num=input("How much points would you like to bet?")
    while(num<0):
        num=input("You can't put in a negative number.")
    if(num>0):
        print("You bet "-num)