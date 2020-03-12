
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
    print("  _______ __      ______              ______                ")
    print(" /_  __(_) /__   /_  __/___ ______   /_  __/___  ___        ")
    print("  / / / / //_/    / / / __ `/ ___/    / / / __ \/ _ \\      ")
    print(" / / / / ,<      / / / /_/ / /__     / / / /_/ /  __/       ")
    print("/_/ /_/_/|_|    /_/  \\__,_/\___/    /_/  \\____/\\___/     ")
    print("                                                            ")
    print("                  By Zachary DeMarco                        ")

# Function to collect user 3 Initials, preventing numbers, and presenting them capitalised. Also recognises "quit" input, forcing the program to quit()
def collectInitials ():
    global userInitials
    # Ask user for Initials
    userInitials = input('Enter your 3 initials: ').upper()
    
    inputProof (userInitials, "Enter your 3 initials: ", False, "Please enter letters only (numbers & special characters invalid)" ,3,"Please enter 3 initials ONLY ", ["anything"],True)


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
    time.sleep(0.5)

# Function that Starts the game. First sorts the gameBoard, then randomly selects a player to begin, and based off of the first player, the user is designagted a symbol.
def gameStart ():

    global playerTurn
    global playersymbol
    global playersymbolPlain
    global computersymbol
    global computersymbolPlain

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
        playersymbol= ("\033[4mO\033[0m")
        playersymbolPlain = "O"
        computersymbol= ("\033[4mX\033[0m")
        computersymbolPlain = "X"
        playerTurn = True

    else:
        print ("You are X's, your move is next.")
        playersymbol= ("\033[4mX\033[0m")
        playersymbolPlain = "X"
        computersymbol= ("\033[4mO\033[0m")
        computersymbolPlain = "O"
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
def inputProof (varib,varibPrompt,isAlphaStatus,isAlphaErr,length,lenErr,ignOpt, *options):

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
        # To prevent possible unforseen error, if something entered makes it this far, an error is printed and the while Loop repeats.
        else:
            while (ignOpt) == False:
                if not (varib.upper()) in options:
                    print("Please chose a valid option.")
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
    nextMoveLetter = inputProof (nextMoveLetter,"Letter: ",False,"Please enter letters only (numbers & special characters invalid) ",1,"Please enter a singular letter: ", ["A","B","C"],False)


    # Collecting the desired number, and checking to make sure it is valid
    nextMoveNumber = input ("Number: ")
    nextMoveNumber = inputProof (nextMoveNumber,"Number: ",True,"Please enter numbers only (letters & special characters invalid) ",1,"Please enter a singular number: ", ["1","2","3"],False)
    
    #convert nextMoveLetter to a numeric Value
    nextMoveLetterNumber= ord(nextMoveLetter)-96

    # Checking to see if the randomly selected coordinates are already taken, if they are, it randomly generates new coordinates
    while not gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] in [(" "),("_")]:
        print ("That spot is already occupied, chose another move: ")

        # Collecting the desired Letter, and checking to make sure its valid
        nextMoveLetter = input ("New Letter: ")
        nextMoveLetter = inputProof (nextMoveLetter,"Letter: ",False,"Please enter letters only (numbers & special characters invalid) ",1,"Please enter a singular letter: ", ["A","B","C"], False)

        # Collecting the desired number, and checking to make sure it is valid
        nextMoveNumber = input ("New Number: ")
        nextMoveNumber = inputProof (nextMoveNumber,"Number: ",True,"Please enter numbers only (letters & special characters invalid) ",1,"Please enter a singular number: ", ["1","2","3"], False)
    
    
    #If statement to differ between needing playersymbolwith an underline or without an underline based on position in grid.
    if int(nextMoveNumber) < 3:
        gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] = playersymbol
        playerTurn = False

    else: 
        gameBoard[int(nextMoveNumber)-1][int(nextMoveLetterNumber)-1] = playersymbolPlain
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
        while not gameBoard[computerNumber][computerLetter] in [(" "),("_")]:
            computerLetter = random.choice([0,1,2])
            computerNumber = random.choice([0,1,2])

        # if the position is valid, the right character to input (with or without underscore) is chosen based on position. 
        if computerNumber <2:
            gameBoard [computerNumber][computerLetter] = computersymbol
            playerTurn = True
        else:
            gameBoard [computerNumber][computerLetter] = computersymbolPlain
            playerTurn = True

    print ("The Computer's Move is: ")
    drawBoard ()

#
def gameWin (symbol,symb):

    return((gameBoard[0][0] == (symbol) and gameBoard[0][1] == (symbol) and gameBoard[0][2] == (symbol)) or #top across
    (gameBoard[1][0]== (symbol) and gameBoard[1][1] == (symbol) and gameBoard[1][2]== (symbol)) or #mid across
    (gameBoard[2][0]== (symb) and gameBoard[2][1] == (symb) and gameBoard[2][2]== (symb)) or # bottom across
    (gameBoard[0][0] == (symbol) and gameBoard [1][0] == (symbol) and gameBoard [2][0]== (symb)) or #left down
    (gameBoard[0][1] == (symbol) and gameBoard [1][1] == (symbol) and gameBoard [2][1]== (symb)) or #mid down
    (gameBoard[0][2] == (symbol) and gameBoard [1][2] == (symbol) and gameBoard [2][2]== (symb)) or #right down
    (gameBoard[0][0] == (symbol) and gameBoard[1][1] == (symbol) and gameBoard[2][2]== (symb)) or #diag top left to bottom right
    (gameBoard[0][2] == (symb) and gameBoard[1][1] == (symbol) and gameBoard [2][0]== (symbol)))  #diag bottom left to top right      

def gamePlay ():
    global moveCount
    global gameStatus
    global tieStatus
    moveCount = 0
    gameStatus = True

    while gameStatus == True:
        if moveCount < 9:
            if playerTurn == True:
                playerTurnAction ()
                moveCount = moveCount + 1
                if gameWin (playersymbol,playersymbolPlain):
                    gameStatus = False
                time.sleep(0.5)
            elif playerTurn == False:
                computerTurnAction ()
                moveCount = moveCount + 1
                if gameWin (computersymbol,computersymbolPlain):
                    gameStatus = False
                time.sleep(0.5)
        elif moveCount == 9:
            gameStatus = False
            tieStatus = True
        

def gameOver ():
    global restartValue

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