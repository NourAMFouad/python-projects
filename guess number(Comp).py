# Gues the number (computer) game 

import random

computer_num = 0
user_num = 0

# start to make the computer choose the random number 
computer_num = random.randint(1, 100)

# make the user guess the number 
print("guess the number from 1 to 100")

#casting user_num to convert from string to integer
# because the defualt of input function is string
user_num = int(input("Enter your number: "))


## just for testing (if program store the correct data or not)
print(user_num)
print(computer_num)

while((user_num >= 1) and (user_num <= 100) ):

    if computer_num < user_num:
        print("Enter the number less than you enter before.")
    elif computer_num > user_num:
       print("Enter the number greater than you enter before.")
    #to end the program when user win 
    elif computer_num == user_num:
        print("The guessing number is correct :)")
        break
    user_num =int(input())
