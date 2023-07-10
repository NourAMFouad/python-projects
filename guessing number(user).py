import random

computer_num = 0
user_num = 0
feedback = ''

# range of number
low = 1
high = 10

# allow user to enter the number 
user_num = int(input("Enter the number between 1 and 10 : "))

while feedback != 'c':
    # make the computer guess the number 
    if low != high :
       computer_num = random.randint(low, high)
    else :
       computer_num = low

    # store the feedback to help the computer to guess the number correctly
    # put lower function to make any charecter the user will enter in lower case 
    feedback = input(f"If {computer_num} is High(H), Low(L) or Correct(C) : " ).lower()

    if feedback == 'l':
        low = computer_num + 1
        
    elif feedback == 'h':
        high = computer_num - 1 

print("congratiolations, the guessing number is correct. :)")  
