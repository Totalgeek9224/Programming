
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

def gameTitle ():
    global gameBoard
    
    print("  _______ __      ______              ______                ")
    print(" /_  __(_) /__   /_  __/___ ______   /_  __/___  ___        ")
    print("  / / / / //_/    / / / __ `/ ___/    / / / __ \/ _ \\      ")
    print(" / / / / ,<      / / / /_/ / /__     / / / /_/ /  __/       ")
    print("/_/ /_/_/|_|    /_/  \\__,_/\___/    /_/  \\____/\\___/     ")
    print("                                                            ")
    print("                  By Zachary DeMarco                        ")
    
    gameBoard = [ [ "E", "E", "E" ], [ "E", "E", "E" ],[ "E", "E", "E" ] ]
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


# Prints the gameboard with appropriate formatting
#(Intermediate function)
def drawBoard ():
    print ("  A B C")
    for rowNo, row in enumerate(gameBoard):
        print (str(rowNo +1), end = " ")
        
        for colNo, col in enumerate (row):
            if rowNo < 2:
                if col == "E":
                    print ("_", end="")
                elif col == "X":
                    print ("\033[4mX\033[0m", end="")
                else:
                    print ("\033[4mO\033[0m",end="")
            else:
                if col == "E":
                    print (" ", end="")
                elif col == "X":
                    print ("X", end="")
                else:
                    print ("O", end="")
            if colNo < 2:
                print ("|", end="")

        time.sleep(0.1)
        print ()

# Function that Starts the game. First sorts the gameBoard, then randomly selects a player to begin, and based off of the first player, the user is designagted a symbol.
def gameStart ():

    global playerTurn
    global playersymbol
    global computersymbol

    #introducing the playerTurn Variable
    playerTurn = False

    #Randomly selecting first player using the Random module
    firstPlay = random.choice(["Player", "Computer"])
    print("The first move goes to: " + firstPlay )

    #Assigning roles based off of first player. 
    if firstPlay == "Player":
        print ("You are O's ")
        playersymbol= ("O")
        computersymbol= "X"
        playerTurn = True

    else:
        print ("You are X's, your move is next.")
        playersymbol= "X"
        computersymbol= "O"
        playerTurn = False
    
    drawBoard ()
#
# Function to proof the input based on certain criteria,  mainly if Quit is entered, if the entered text is alphanumeric, if the entered text is a certain length, and if the entered text is within a certain list
#   varib: the variable that you are checking
#   varibPrompt: the prompt given to users to ask for Varib upon condition check failure
#   isAlphaStatus: (BOOL) whether the input you are expecting is alphanumeric or not
#   isAplhaErr: the error that is thrown when the input doesnt meet the condition of isAlphaStatus
#   length:(int) the desired length of the input
#   lenErr: the error that is printed when the input isnt of the desired length
#   options: [list] the desired inputs that pass the proof function. If it's not one of these inputs, the function will just loop.
def inputProof (varib,varibPrompt,isAlphaStatus,isAlphaErr,length,lenErr, options):

    while not varib.upper() in options:
        # Implementation of Quit function to allow for quitting throughout process
        if varib.upper() == ("QUIT"):
            print ("Quitting Program")
            quit ()
        # Using .isalpha command to filter letters only, if not only letters, error is printed
        elif varib.isalpha() == isAlphaStatus:
            print (isAlphaErr)
            varib = input (varibPrompt)
        # Ensuring varib is only len character(s) long, if not, an error is printed
        elif (len(varib) != length):
            print(lenErr)
            varib = input (varibPrompt)
        # Vetting to ensure the entered input is a valid option.
        elif not (varib.upper()) in options:
            print("Please chose a valid option.")
            varib = input (varibPrompt)
        # To prevent possible unforseen error, if something entered makes it this far, an error is printed and the while Loop repeats.
        else:
            print('Incorrect Formatting- Please try again')
            varib = input (varibPrompt)

    return varib
# Based off of the users input, this function writes their move to the gameBoard, and then uses the drawBoard function to print the board.
def playerTurnAction ():

    global nextMoveLetter
    global nextMoveNumber
    global playerTurn

    #collect desired user position
    print ("Where would you like to place your piece? ")
    
    # Collecting the desired Letter, and checking to make sure its valid
    nextMoveLetter = input ("Letter: ")
    nextMoveLetter = inputProof (nextMoveLetter,"Letter: ",False,"Please enter letters only (numbers & special characters invalid) ",1,"Please enter a singular letter: ", ["A","B","C"])


    # Collecting the desired number, and checking to make sure it is valid
    nextMoveNumber = input ("Number: ")
    nextMoveNumber = inputProof (nextMoveNumber,"Number: ",True,"Please enter numbers only (letters & special characters invalid) ",1,"Please enter a singular number: ", ["1","2","3"])
    
    #convert nextMoveLetter to a numeric Value
    nextMoveLetterNumber= ord(nextMoveLetter)-96

    # Checking to see if the randomly selected coordinates are already taken, if they are, it randomly generates new coordinates
    while not gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] in ["E"]:
        print ("That spot is already occupied, chose another move: ")
        # Collecting the desired Letter, and checking to make sure its valid
        nextMoveLetter = input ("New Letter: ")
        nextMoveLetter = inputProof (nextMoveLetter,"Letter: ",False,"Please enter letters only (numbers & special characters invalid) ",1,"Please enter a singular letter: ", ["A","B","C"])
        return nextMoveLetter
        # Collecting the desired number, and checking to make sure it is valid
        nextMoveNumber = input ("New Number: ")
        nextMoveNumber = inputProof (nextMoveNumber,"Number: ",True,"Please enter numbers only (letters & special characters invalid) ",1,"Please enter a singular number: ", ["1","2","3"])
        return nextMoveNumber
    
   
    gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] = playersymbol
    playerTurn = False

    print ("Your move is:")
    drawBoard()

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
        while not gameBoard[computerNumber][computerLetter] in ["E"]:
            computerLetter = random.choice([0,1,2])
            computerNumber = random.choice([0,1,2])

       
        gameBoard [computerNumber][computerLetter] = computersymbol
        playerTurn = True

    print ("The Computer's Move is: ")
    drawBoard ()

#
def gameWin (symbol):

    return((gameBoard[0][0] == (symbol) and gameBoard[0][1] == (symbol) and gameBoard[0][2] == (symbol)) or #top across
    (gameBoard[1][0]== (symbol) and gameBoard[1][1] == (symbol) and gameBoard[1][2]== (symbol)) or #mid across
    (gameBoard[2][0]== (symbol) and gameBoard[2][1] == (symbol) and gameBoard[2][2]== (symbol)) or # bottom across
    (gameBoard[0][0] == (symbol) and gameBoard [1][0] == (symbol) and gameBoard [2][0]== (symbol)) or #left down
    (gameBoard[0][1] == (symbol) and gameBoard [1][1] == (symbol) and gameBoard [2][1]== (symbol)) or #mid down
    (gameBoard[0][2] == (symbol) and gameBoard [1][2] == (symbol) and gameBoard [2][2]== (symbol)) or #right down
    (gameBoard[0][0] == (symbol) and gameBoard[1][1] == (symbol) and gameBoard[2][2]== (symbol)) or #diag top left to bottom right
    (gameBoard[0][2] == (symbol) and gameBoard[1][1] == (symbol) and gameBoard [2][0]== (symbol)))  #diag bottom left to top right      

def gamePlay ():
    global moveCount
    global gameStatus
    global tieStatus

    tieStatus = False

    moveCount = 0
    gameStatus = True

    while gameStatus == True:
        if moveCount < 9:
            if playerTurn == True:
                playerTurnAction ()
                moveCount = moveCount + 1
                if gameWin (playersymbol):
                    gameStatus = False
                time.sleep(0.5)
            elif playerTurn == False:
                computerTurnAction ()
                moveCount = moveCount + 1
                if gameWin (computersymbol):
                    gameStatus = False
                time.sleep(0.5)
        elif moveCount == 9:
            gameStatus = False
            tieStatus = True
        

def gameOver ():
    global restartValue
    global tieStatus

    if tieStatus == True:
        print ("Game Over - Tie!")
        restartValue = input ("Would you like to play again? (Y/N): ")
        
    else:
        if playerTurn == False:
            print ("The Player has won in " + str(moveCount) + " moves!")
            restartValue = input ("Would you like to play again? (Y/N): ")
        else:
            print ('The computer has won in ' + str(moveCount) + ' moves! Better luck next time!')
            restartValue = input ("Would you like to play again? (Y/N): ")

#####################################################
##################### Main Code #####################
#####################################################
restartValue = "Y"
while restartValue.upper() == "Y": 
    gameTitle ()
    collectInitials ()
    gameStart ()
    gamePlay ()
    gameOver ()

print ("Thanks for playing " + userInitials + "!")