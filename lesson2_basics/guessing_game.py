#input
secret = 10
guess = int(input("Guess a number: "))

#Guess
if guess == secret:
    print("you are correct")
elif guess > secret:
    print("too hight")
else:
    print("guess is too low")
