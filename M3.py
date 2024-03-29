import random

BOUNDS = (1, 100)
TRIES_ALLOWED = 5

the_number = random.randint(*BOUNDS)

print("\tWelcome to 'Guess My Number'!\n")
print("I'm thinking of a number between %d and %d." % BOUNDS)
print("Try to guess it in as few attempts as possible.\n")

for tries in range(TRIES_ALLOWED):
    guess = int(input("Take a guess: "))

    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("You guessed it! The number was %d" % (the_number))
        print("And it only took you %d tries!\n\n" % (tries + 1))
        break
else:
    print("You failed to guess in time!\n\n")

