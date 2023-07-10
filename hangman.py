import random

#list of words
#words = ["available","average","avoid","awake","aware","awesome","awful","axiomatic","babies","baby","back","bad","badge","bag","bait","bake","balance","ball","ban","bang","barbarous","bare","base","baseball","bashful","basin","basket","basketball","bat","bath","bathe","battle","bawdy","bead","beam","bear","beautiful","bed","bedroom","beds","bee","beef","befitting","beg","beginner","behave","behavior","belief","believe","bell","belligerent","bells","belong","beneficial","bent","berry","berserk","best","better","bewildered","big","bike","bikes","billowy","bird","birds","birth","birthday","bit","bite","bite-sized","bitter","bizarre","black","black-and-white","blade","bleach","bless","blind","blink","blood","bloody","blot","blow","blue","blue-eyed","blush","blushing","board","boast","boat","boil","boiling","bolt","bomb","bone","book","books","boorish","boot","border","bore","bored","boring","borrow","bottle","bounce","bouncy","boundary","boundless","bow","box","boy","brainy","brake","branch","brash","brass","brave","brawny","breakable","breath","breathe","breezy","brick","bridge","brief","bright","broad","broken","brother","brown","bruise","brush","bubble","bucket","building","bulb","bump","bumpy","burly","burn","burst","bury","bushes","business","bustling","busy","butter","button","buzz","cabbage","cable","cactus","cagey","cake","cakes","calculate","calculating","calculator","calendar","call","callous","calm","camera","camp","can","cannon","canvas","cap","capable","capricious","caption","car","card","care","careful","careless","caring","carpenter","carriage","carry","cars","cart","carve","cast","cat","cats","cattle","cause","cautious","cave","ceaseless","celery","cellar","cemetery","cent","certain","chalk","challenge","chance","change","changeable","channel","charge","charming","chase","cheap","cheat","check","cheer","cheerful","cheese","chemical","cherries","cherry","chess","chew","chicken","chickens","chief","childlike","children","chilly","chin","chivalrous","choke","chop","chubby","chunky","church","circle","claim","clam","clammy","clap","class","classy","clean","clear","clever","clip","cloistered","close","closed","cloth","cloudy","clover","club","clumsy","cluttered","coach","coal","coast","coat","cobweb","coherent","coil","cold","collar","collect","color","colorful","colossal","colour","comb","combative","comfortable","command","committee","common","communicate","company","compare","comparison","compete","competition","complain","complete","complex","concentrate","concern","concerned","condemned","condition","confess","confuse","confused","connect","connection","conscious","consider","consist","contain","continue","control","cooing","cook","cool","cooperative","coordinated","copper","copy","corn","correct","cough","count","country","courageous","cover","cow"]
words = ["available","average","avoid"]

# to store the list of letters that user used when play 
used_letters = []
# allow computer to choose the random word
# store it computer_word variable 
computer_word = random.choice(words)

# for testing 
#print(computer_word)

# to store number  of attempts to play when it = 0 then the user loss
number_of_attempts = 7

# to store the letters by using _ 
guessing_word = ""

# to store the letter that the user guess
letter =''


# put guessing_word = computer_word 
# and replace all letters in guessing_word variable into _
#guessing_word = computer_word

##guessing_word = ''.join('_' for _ in computer_word)
#alternative from the previous statment
guessing_word = '_'*len(computer_word)
# for testing 
print(guessing_word)

find = False

while ('_' in guessing_word and number_of_attempts != 0):
   
    # Allow user to enter the value of letter variable in upper case
    letter = input("Enter the guessing letter : ")

    # check if computer_word include the letter that user enter or not
    for ind, char in enumerate(computer_word):
        if letter == char:
        # it means the computer_word include the letter
        # so replace the _ in guessing_word with the same index like computer_word variable
            guessing_word = guessing_word[:ind] + letter + guessing_word[ind+1:]
        
        # add the letter in the list used_list
            used_letters.append(letter)
            find = True
        
    # to store all the elements that user was enter
    used_letters.append(letter)

    if find:  # it means the number of attempts not decrease
        print(f"You used : {set(used_letters)} letters")
        print(f"The word : {guessing_word} and Your number of attempts = {number_of_attempts}")
    else: # it means number of attempts must decrease because the guessing not correct
        number_of_attempts = number_of_attempts - 1
        print(f"You used : {set(used_letters)} letters")
        print(f"OOOh,The word : {guessing_word} and Your number of attempts = {number_of_attempts}")
    
    # to make the find variable in initiale state before start the new iteration 
    find = False


if computer_word in guessing_word :
    print("You win :)")
    print(f"The word is {guessing_word}")
else :
    print("You loss, sorry.")
    print(f"The word is {computer_word}")
