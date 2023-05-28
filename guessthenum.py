import random
num= random.randint(1,100)
tries=0
print("Guess the number I am thinking it's between 1 & 100:")
while True:
    guess= int(input("Your guess?\n"))
    tries+=1
    if num > guess:
        print("it's not this low .Try Again")
    elif num < guess:
        print("it's not this high.Try Again")
    else:
        print("HORRAY!! You guessed it Right in ",tries,"Attempts")
        break

