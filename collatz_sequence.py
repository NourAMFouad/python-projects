# This project from AUTOMATE THE BORING STUFF WITH PYTHON AUTOMATE THE BORING STUFF WITH PYTHON book 
# page 77 

number_type = ""
calc = 0

def collatz (number):
    # to make the calc varieble is global 
    # if you want to make any variable is global to use it in any scope 
    # you must write the global statment 
    global calc
    global number_type
    # to check the number if it even or odd 
    #if number is even 
    if number % 2 == 0:
        calc = number // 2
        number_type = "even"
    # if number is odd
    elif number % 2 == 1:
        calc =  3*number+1
        number_type = "odd"
    return calc
    
while (calc != 1):
    try:
        # allow user to enter the number 
        number = int(input("Enter the number : "))
        print(collatz(number))
        print(f"Your number {number} is {number_type}")
        # just for test if calc store the correct values or not 
        #print(calc)
    except:
        print("You must enter the integer number")
print("See you later :)")

# takecare the following code
#    print(collatz(number))
#    print(f"Your number {number} is {number_type}")
#    just for test if calc store the correct values or not 
#    print(calc)
#  should write in the try scope 