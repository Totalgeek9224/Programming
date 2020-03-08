
import random
import time
##############################################################
##################### Declare Statements #####################
##############################################################
userInitials = []
gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ],[ "E", "E", "E" ] ]
gameStatus = True
moveCount = 0
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
        # Using .isalpha command to filter letters only, if not only letters, error is printed
        elif userInitials.isalpha() == False:
            print ("Please enter letters only (numbers & special characters invalid) ")
            userInitials = input('Enter your 3 initials: ').upper()
        # Ensuring userInitials are only 3 characters long, if the length of userInitials is not equal to 3, an error is printed
        elif (len(userInitials) != 3):
            print("Please enter 3 initials ONLY ")
            userInitials = input('Enter your 3 initials: ').upper()
        # To prevent possible unforseen error, if something entered makes it this far, an error is printed and the while Loop repeats.
        else:
            print('Incorrect Formatting- Please try again')
            userInitials = input('Enter your 3 initials: ').upper()

    # Print out confirmation of userInitials
    print ("Your initials are: " + userInitials)

# Function to redefine gameBoard values in order to make it formatted for TicTacToe grid
#(Intermediate function)
def gameBoardSort ():
    global gameBoard
    #Reassigning gameBoard values to represent ideal blank grid
    gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ],[ "E", "E", "E" ] ]
    for x in gameBoard:
        gameBoard[0] = ["_", "_", "_"]
        gameBoard[1] = ["_", "_", "_"]
        gameBoard[2] = [" ", " ", " "]

# Prints the gameboard with appropriate formatting
#(Intermediate function)
def drawBoard ():
    print ("  A B C")
    print ("1", end =" ")
    print(*gameBoard[0], sep = "|")
    print ("2", end =" ")
    print(*gameBoard[1], sep = "|")
    print ("3", end =" ")
    print(*gameBoard[2], sep = "|")  
    time.sleep(1)

# Function that Starts the game. First sorts the gameBoard, then randomly selects a player to begin, and based off of the first player, the user is designagted a symbol.
def gameStart ():

    global playerTurn
    global playerSymbol
    global playerSymbolPlain
    global computerSymbol
    global computerSymbolPlain

    #activates the sort funtion in order to redifine the list values into plain TicTakToe formatting
    gameBoardSort ()
    #introducing the playerTurn Variable
    playerTurn = False

    #Randomly selecting first player using the Random module
    firstPlay = random.choice(["Player", "Computer"])
    print("The first move goes to: " + firstPlay )

    #Assigning roles based off of first player. 
    if firstPlay == "Player":
        print ("You are O's ")
        playerSymbol = ("\033[4mO\033[0m")
        playerSymbolPlain = "O"
        computerSymbol = ("\033[4mX\033[0m")
        computerSymbolPlain = "X"
        playerTurn = True

    else:
        print ("You are X's, your move is next.")
        playerSymbol = ("\033[4mX\033[0m")
        playerSymbolPlain = "X"
        computerSymbol = ("\033[4mO\033[0m")
        computerSymbolPlain = "O"
        playerTurn = False
    
    drawBoard ()

# Based off of the users input, this function writes their move to the gameBoard, and then uses the drawBoard function to print the board.
def playerTurnAction ():

    global nextMoveLetter
    global nextMoveNumber
    global playerTurn

    #collect desired user position
    print ("Where would you like to place your piece? ")
    
    # Collecting the desired Letter, and checking to make sure its valid
    nextMoveLetter = input ("Letter: ")
    while (nextMoveLetter.isalpha() == False) or (nextMoveLetter.upper() == ("QUIT")) or (len(nextMoveLetter) !=1) or not (nextMoveLetter.upper()) in ["A","B","C"]:
        # Implementation of Quit function to allow for quitting throughout process
        if nextMoveLetter.upper() == ("QUIT"):
            print ("Quitting Program")
            quit ()
        # Using .isalpha command to filter letters only, if not only letters, error is printed
        elif nextMoveLetter.isalpha() == False:
            print ("Please enter letters only (numbers & special characters invalid) ")
            nextMoveLetter = input ("Letter: ")
        # Ensuring userMoverLetter is only 1 character long, if not, an error is printed
        elif (len(nextMoveLetter) != 1):
            print("Please enter a singular letter: ")
            nextMoveLetter = input ("Letter: ")
        # Vetting to ensure the entered input is a valid option.
        elif not (nextMoveLetter.upper()) in ["A","B","C"]:
            print("Please chose a valid option. Either A, B, or C ")
            nextMoveLetter = input ("Letter: ")
        # To prevent possible unforseen error, if something entered makes it this far, an error is printed and the while Loop repeats.
        else:
            print('Incorrect Formatting- Please try again')
            nextMoveLetter = input ("Letter: ")

    # Collecting the desired number, and checking to make sure it is valid
    nextMoveNumber = input ("Number: ") 
    while (nextMoveNumber.isalpha() == True) or (nextMoveNumber.upper() == ("QUIT")) or (len(nextMoveNumber) !=1) or not (nextMoveNumber) in ["1","2","3"]:
        # Implementation of Quit function to allow for quitting throughout process
        if (nextMoveNumber.upper()) == ("QUIT"):
            print ("Quitting Program")
            quit ()
        # Using .isalpha command to filter letters only, if not only letters, error is printed
        elif nextMoveNumber.isalpha() == True:
            print ("Please enter numbers only (letters & special characters invalid) ")
            nextMoveNumber = input ("Number: ")
        # Ensuring nextMoveNumber are only 1 character long, if it is not, an error is thrown
        elif (len(nextMoveNumber) != 1):
            print("Please enter a singular number: ")
            nextMoveNumber = input ("Number: ")
        # Vetting to ensure the entered input is a valid option.
        elif not (nextMoveNumber) in ["1","2","3"]:
            print("Please chose a valid option. Either 1,2, or 3 ")
            nextMoveNumber = input ("Number: ")
        # To prevent possible unforseen error, if something entered makes it this far, an error is printed and the while Loop repeats.
        else:
            print('Incorrect Formatting- Please try again')
            nextMoveNumber = input ("Number: ")

    #convert nextMoveLetter to a numeric Value
    nextMoveLetterNumber= ord(nextMoveLetter)-96

    #If statement to differ between needing playerSymbol with an underline or without an underline based on position in grid.
    if int(nextMoveNumber) < 3:
        gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] = playerSymbol
        playerTurn = False

    else: 
        gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] = playerSymbolPlain
        playerTurn = False

    print ("Your move is:")
    drawBoard ()

# When it's the computer's turn, this function randomly choses a position on the board, then checks to see if it's valid. If it is, it plays the move, otherwise, it randomly generates until it gets a valid move
def computerTurnAction ():
    global computerLetter
    global computerNumber
    global playerTurn

    while playerTurn == False:
        # Randomly selecting computer Letter
        computerLetter = random.choice([0,1,2])
        # Randomly selecting computer Number
        computerNumber = random.choice([0,1,2])

        # Checking to see if the randomly selected coordinates are already taken, if they are, it randomly generates new coordinates
        if not gameBoard[computerNumber][computerLetter] in [(" "),("_")]:
            computerLetter = random.choice([0,1,2])
            computerNumber = random.choice([0,1,2])
        # if the position is valid, the right character to input (with or without underscore) is chosen based on position. 
        else:
            if computerNumber <2:
                gameBoard [computerNumber][computerLetter] = computerSymbol
                playerTurn = True
            else:
                gameBoard [computerNumber][computerLetter] = computerSymbolPlain
                playerTurn = True

    print ("The Computer's Move is: ")
    drawBoard ()

#
def gameWin ():
    gameOver = False  
    while gameOver == False:
        return ((gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2])or #top across
        (gameBoard[1][0]== gameBoard[1][1] == gameBoard[1][2]) or #mid across
        (gameBoard[2][0]== gameBoard[2][1] == gameBoard[2][2]) or # bottom across
        (gameBoard[0][0] == gameBoard [1][0] == gameBoard [2][0]) or #left down
        (gameBoard[0][1] == gameBoard [1][1] == gameBoard [2][1]) or #mid down
        (gameBoard[0][2] == gameBoard [1][2] == gameBoard [2][2]) or #right down
        (gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]) or #diag top left to bottom right
        (gameBoard[0][2] == gameBoard[1][1] == gameBoard [2][0]))  #diag bottom left to top right
        
#####################################################
##################### Main Code #####################
#####################################################
print("  _______ __      ______              ______                ")
print(" /_  __(_) /__   /_  __/___ ______   /_  __/___  ___        ")
print("  / / / / //_/    / / / __ `/ ___/    / / / __ \/ _ \\      ")
print(" / / / / ,<      / / / /_/ / /__     / / / /_/ /  __/       ")
print("/_/ /_/_/|_|    /_/  \\__,_/\___/    /_/  \\____/\\___/     ")
print("                                                            ")
print("                  By Zachary DeMarco                        ")

collectInitials ()
gameStart ()
while gameStatus == True:
    if moveCount < 9:
        if playerTurn == True:
            playerTurnAction ()
            moveCount = moveCount + 1
            time.sleep(1)
        else:
            computerTurnAction ()
            moveCount = moveCount + 1
            time.sleep(1)
    else:
        print ("Game Over - Tie!")
        gameStatus = False