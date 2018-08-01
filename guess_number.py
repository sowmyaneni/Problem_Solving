# The computer will find the number you are guessing
low = 0
high = 100
mid = (low+high)//2

print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number {}?".format(mid))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess == 'h':
        high = mid
    elif guess == 'l':
        low = mid
    elif guess == 'c':
         break
    else:
        print("Sorry, I did not understand your input.")
    mid = (low + high)//2
print("Game Over. Your secret number was {}.".format(mid))
