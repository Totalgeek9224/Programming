
import random
##############################################################
##################### Declare Statements #####################
##############################################################
userInitials = []
gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ],[ "E", "E", "E" ] ]
firstMove = []
#####################################################
##################### Functions #####################
#####################################################

# Function to collect user 3 Initials, preventing numbers, and presenting them capitalised. Also recognises "quit" input, forcing the program to quit
def collectInitials ():

    # Ask user for Initials
    userInitials = input('Enter your 3 initials: ').upper()
    if userInitials == ("quit" or "Quit"):
        quit()

    # Confirm only letters
    while (userInitials.isalpha() == False) or not (len(userInitials) == 3):
        print('Incorrect Formatting- Please try again')
        userInitials = input('Enter your 3 initials: ').upper()
        if userInitials == ("quit" or "Quit"):
            quit()

    print ("Your initials are:" + userInitials)

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
print('''\  
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