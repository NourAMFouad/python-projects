import random

# alow user to choose from list (R-P-S)
user_choice = ''

#Allow computer to choose form the list (R-P-S)
# using random module to do this 
# and store the char in variable 
listOfchoices = ['r', 's', 'p']

while user_choice != 'e':
    user_choice = input("Choose the character R for Rock, P for paper and S for scissors Or enter e to end the game : ").lower()
    computer_choice = random.choice(listOfchoices)

    #1
    if  (user_choice == 'r' and computer_choice == 's' ) or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print(f"Your choice {user_choice} and Computer choice {computer_choice}, So You Win :)")
    #2
    elif  (computer_choice == 'r' and  user_choice == 's') or (computer_choice == 's' and  user_choice == 'p') or (computer_choice == 'p' and  user_choice == 'r'):
        print(f"Your choice {user_choice} and Computer choice {computer_choice}, So Computer Win.")
    #3
    elif (user_choice == computer_choice):
        print(f"Your choice {user_choice} and Computer choice {computer_choice}, So no one win, your are even")
print("You end the game, goodbye.")


#1 if  (User_choice == r and computer_Choice == s ) or (User_choice == s and computer_Choice == p) or (User_choice == p and computer_Choice == r) 
# then user win

#2 if  (computer_choice == r and  user_Choice == s) or (computer_choice == s and  user_Choice == p) or (computer_choice == p and  user_Choice == r)
# then computer win

#3 check if User_choice == computer_Choice 
# then even // tie 

# to stop game (loop) enter e


####NOte###
#in this problem you can remove the 2 condition and write else only 
# to make your code more clean and donot repeat some statments 