import random

print("Find a random number")

print("For a better gameplay choose a range")
while True:
    try:
        minimum = int(input("Set the minimum number: "))
        maximum = int(input("Set the maximum number: "))
    except ValueError:
        print("You wrote something wrong")
    if minimum > maximum:
        print("The max number must be higher than min number")
    else:
        break



print()

rand_num = random.randint(minimum, maximum)
 
attempt = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not an integer, try again")
        continue
        
    if guess > maximum or guess < minimum:
        print("You are out of the number range, try again")
        continue

    if guess > rand_num:
        print("Too high, try lower")
        attempt +=1
    elif guess < rand_num:
        print("Too low, try higher")
        attempt +=1
    else:
        attempt +=1
        print("Congrats, you found the number!")
        print(f"The number was {rand_num}, you found it in {attempt} attempts!")
        break

