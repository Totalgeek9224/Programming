# Function to print the Leader Board Data, or to initialise the gameboard file. 
leaderBoard = []

def readLeaderBoard ():
    global leaderBoard


    try:
        with open("leaderBoard.dat", "r") as f:
            leaderBoard = f.readline().strip()
            while leaderBoard:
                players= leaderBoard.split("\n")
                try:
                    leaderBoard.append([str(userInitals[0]), int(noOfWins[1]), int(noOfLosses[3]), int(noOfGames[0])])
                except FileNotFoundError:
                    print ("leaderBoard.dat is corrupted")
                    quit ()
                else:
                    leaderBoard = f.readline().split()
            
            
           
    
    except FileNotFoundError:
        
        try:
            with open("leaderBoard.dat", "w+") as f:
                leaderBoard = []

        except Exception:
            print ("Failed to create leaderBoard.dat")
    
    #except Exception:
        #print (" Failed to access leaderBoard.dat")
    

def displayLeaderBoard ():
    with open("leaderBoard.dat", "r") as f:
        print ("\033[4mPlayer\033[0m" " " "\033[4mWins\033[0m" " " "\033[4mDraws\033[0m" " " "\033[4mLosses\033[0m" " " "\033[4mTotal Games Played\033[0m" " " "
        for leaderBoard in f:
            print (leaderBoard)

    
def writeLeaderBoard ():
    global userInitals

    with open ("leaderBoard.dat", "r+") as l:
        players = [playerInitials.upper(), noOfWins, noOfDraws, noOfLosses, noOfGames]
        for player in players:
            l.write(str(player() + "    ")
    except Exception:
        print ("Unable to sucesssfully write to leaderBoard.dat")

    #if userInitals in leaderBoard:
        #try:
            #with open ("leaderBoard.dat", "r+") as l:
                #players = [playerInitials.upper, noOfWins,noOfDraws, noOfLosses, noOfGames]
                #for player in players:
                    #leaderBoard.write(str(player) + "   ")
        #except:
            #pass

readLeaderBoard ()
displayLeaderBoard()
#writeLeaderBoard ()