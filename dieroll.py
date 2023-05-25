import random
num_roll =int(input("How many times do you want to roll the die? ")) 
for i in range(num_roll):
    result = random.randint(1, 6)
    print("The die rolled:", result)
