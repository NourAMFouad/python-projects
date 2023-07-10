#import sys

global player 
global opponent 
global not_found 
 #     row1 (0)        row2  (1)       row3  (2)
board =[ ['1','2', '3'],['4','5', '6'],['7','8', '9']]

# initialize the board (3*3) of play when start the game
# like this 
#    - - - 
#    - - -  
#    - - -
#board[3][3] =[
 #       ['-','-', '-'],
  #      ['-','-', '-'],
   #     ['-','-', '-']
    #]
def init_board():
    global board 

    # or use loop and join function
    for row in board:
        # the join() function is used to concatenate the elements of each row with a space (' ') as the separator
         print(' '.join(row))
    
   # when we need to print the board without square practice
   # we can do this manual way
   #  for row in board:
    #   for cell in row:
    #      print(cell, end=' ')
    #      print()  


# initialize players
# to determain players who is X and O
def initialize_players (player):

        if player == 'x':
            opponent = 'o'
            print(f"Now you is {player} player and your oppnent is {opponent} .")
        elif player == 'o':
            opponent = 'x'
            print(f"Now you is {player} player and your oppnent is {opponent} .")
        else :
            print("Please enter the correct char, choose (X OR O) only :")
            player1 = input()
            initialize_players(player1)

       
    
# game , switch the players
# play --> the number of place that the user want to play on it 
# value_of_play --> X or O
 
def play(play_place, value_of_play):
   # We assume the place not empty until not_found = False 
   not_found = True 
   # to make user enter X or O only and the number of place from 1 to 9
   if play_place in ['1','2','3','4','5','6','7','8','9'] and value_of_play in ['x','o'] :
        # check of the place and put the new value on it 
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == play_place:
                        board[row][column] = value_of_play
                        not_found = False 
                        break
        if not_found == True :
            print("This place is full, try Again .")
            player = input("Enter your player X or O : ")
            place = input("Enter place :  ")
            play(place, player)
       
   else :
        print("Try agian, with the correct input, place 1 -> 9 and symbol x or o only.")
        player = input("Enter your player X or O : ")
        place = input("Enter place :  ")
        play(place, player)


       
                




# statues to win 
# Take the board list and player_to_check -->(X or O)
# statues_to_win function return True or False
#       True if board include empty places and No one win 
#       False if  board Full or any player win 
def statues_to_win(board, player_to_check):
    counter = 0
    # First state if elemetns of any row from the board are equals with the same symple 
    # Second state if elemetns of any columns from the board are equals with the same symple
    # Third state if elemetns of any diagonal from the board are equals with the same symple
    # another state if no element from the board is empty and no one win 
    #     so the both player are equal.

    # First state 
    #   row 1 
    if ((board[0][0] == board[0][1]) and (board[0][1] == board[0][2])):
        print(f"the {player_to_check} is win :)")
        return False
    #   row 2
    elif ((board[1][0] == board[1][1]) and (board[1][1] == board[1][2])):
        print(f"the {player_to_check} is win :)")
        return False
    #   row 3
    elif ((board[2][0] == board[2][1]) and (board[2][1] == board[2][2])):
        print(f"the {player_to_check} is win :)")
        return False
    # Second state
    #   column 1
    elif ((board[0][0] == board[1][0]) and (board[1][0] == board[2][0])):
        print(f"the {player_to_check} is win :)")
        return False
    #   column 2
    elif ((board[0][1] == board[1][1]) and (board[1][1] == board[2][1])):
        print(f"the {player_to_check} is win :)")
        return False
    #   column 3
    elif ((board[0][2] == board[1][2]) and (board[1][2] == board[2][2])):
        print(f"the {player_to_check} is win :)")
        return False
    # Third state
    #    daigonal 1
    elif ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2])):
        print(f"the {player_to_check} is win :)")
        return False
    #    daigonal 2
    elif ((board[2][0] == board[1][1]) and (board[1][1] == board[0][2])):
        print(f"the {player_to_check} is win :)")
        return False
    
    # onther state 
    #  to check if boerd is empty or not 
    for row in board:
        for element in row:
            if (element == 'x' or element == 'o'):
                counter +=1
    # if counter is 9 then it means the board not include the empty place to play 
    if (counter == 9):
        print("No one win :{ ")
        return False
        #sys.exit()
    else :
        return True

# This function to switch the player
# to allow player play once only 
def switch_player (last_play_symbol):
    if last_play_symbol == 'x':
        print(f"This is o play .")
        return 'o'
    elif last_play_symbol == 'o':
        print(f"This is x play .")
        return 'x'


# function to start play 
def main_fun ():
    print("Start to play --> ")
    # Allow user to choose the symbol to start the play 
    player = input("Enter your symbol X OR O : ")
    initialize_players(player)

    # to print the board 
    init_board()
    # To initialize the state variable 
    # statues_to_win function return True or False    
    state = True
    last_play = ' '

    while state :
    
        # Allow user to enter the charcter and the place that he want to play 
        player = input("Enter your player X or O : ")
        if last_play != player :
            place = input("Enter place :  ")
            # to replace the number of place in board and put he is X or O
            play(place ,player)
            # to check who is win?
            state = statues_to_win(board, player)

            init_board()
            last_play = player

        elif last_play == player:
            if last_play == 'x':
                print("Sorry, this not X play :: make o player play")
                continue
            elif last_play == 'o':
                print("Sorry, this not o play :: make X player play")
                continue

# This scope using to test 

# main function dtart to play
main_fun()

# calling function and testing them individual  
#init_board()
#player = input("Enter your player X or O : ")
#initialize_players(player)
#init_board()
#statues_to_win(board, player)
#play('3','x')
#for row in board:
 #   for cell in row:
  #      print(cell, end=' ')
  #  print('')

# test statues_to_win() function 
#state = statues_to_win(board, 'x')
#while state :
 #   print("True ")
 #   state = statues_to_win(board, 'x')


