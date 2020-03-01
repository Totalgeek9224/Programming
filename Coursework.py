
import random
##############################################################
##################### Declare Statements #####################
##############################################################
userInitials = []
gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ],[ "E", "E", "E" ] ]
#####################################################
##################### Functions #####################
#####################################################

# Function to collect user 3 Initials, preventing numbers, and presenting them capitalised. Also recognises "quit" input, forcing the program to quit()
def collectInitials ():
    global userInitials
    # Ask user for Initials
    userInitials = input('Enter your 3 initials: ').upper()
    
    while (userInitials.isalpha() == False) or (userInitials == ("QUIT")) or (len(userInitials) != 3):
        # Implementation of Quit function to allow for quitting throughout process
        if userInitials == ("QUIT"):
            print ("Quitting Program")
            quit ()
        # Using .isalpha command to filter letters only, if not only letters, error is thrown
        elif userInitials.isalpha() == False:
            print ("Please enter letters only (numbers & special characters invalid) ")
            userInitials = input('Enter your 3 initials: ').upper()
        # Ensuring userInitials are only 3 characters long, if the length of userInitials is not equal to 3, an error is thrown
        elif (len(userInitials) != 3):
            print("Please enter 3 initials ONLY ")
            userInitials = input('Enter your 3 initials: ').upper()
        # To prevent possible unforseen error, if something entered makes it this far, an error is thrown and the while Loop repeats.
        else:
            print('Incorrect Formatting- Please try again')
            userInitials = input('Enter your 3 initials: ').upper()

    # Print out confirmation of userInitials
    print ("Your initials are: " + userInitials)

def drawBoard ():
    print ("  A B C")
    print ("1 " + gameBoard[1] + "|" + gameBoard[2] + "|" + gameBoard[3])
    print ("2 _|_|_")
    print ("3 _|_|_")


def gameStart ():

    firstPlay = random.choice(["Player", "Computer"])
    print("The first move goes to: " + firstPlay )

    if firstPlay == "Player":
        print ("You are O's ")
        firstMove = input ("Where would you like your first move?: ")

    else:
        print ("You are X's, your move is next.")

#####################################################
##################### Main Code #####################
#####################################################
print('''  
  _______ __      ______              ______         
 /_  __(_) /__   /_  __/___ ______   /_  __/___  ___ 
  / / / / //_/    / / / __ `/ ___/    / / / __ \/ _ \\
 / / / / ,<      / / / /_/ / /__     / / / /_/ /  __/
/_/ /_/_/|_|    /_/  \__,_/\___/    /_/  \____/\___/     

                  By Zachary DeMarco                 
                                                
                                                             ''')

collectInitials ()
gameStart ()
#drawBoard ()