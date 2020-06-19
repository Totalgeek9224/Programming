# Program that fufils the expectations as set out by the 19-20 Coursework. This includes:
# - Reading in a file "reservation.dat"
# - Feature an Interactive Menu system
# - Display Seat reservations
# - Allow the creation of seat reservations
# - Output the "reservation.dat" file

#Author: Zachary DeMarco for LJMU 3106 FNDET

import json
import time

userKill = None

#####################################################################################################
##########Functions##################################################################################
#####################################################################################################

# Function to read the resevation.dat file, and create such a file if it does not exist 
def checkreservation ():
    try: 
        with open ("reservation.dat", "r") as f:
            json.load(f)
    except FileNotFoundError:
        print ("ERROR: Reservation file missing!")
        print("Please ensure it is in the correct location")
        quit

#Function to print Menu of Options
def printMenu ():
    global menuChoice

    print ("Please select from the following options:")
    print ("1. Display Seat Reservations")
    print ("2. Reserve a Seat")
    print ("3. Quit")
    menuChoice = input ("")

#Function to Prompt repeating Menu of options
def callMenu ():
    global menuChoice

    while userKill == False:
        printMenu ()
        if menuChoice == "1" or "2" or "3":
            if 

        else:
            print ("That's not a recognised input. Please enter 1, 2 or 3.")
            menuChoice = ""
            time.sleep (1.5)
            print ("")
            continue



checkreservation ()
userKill = False
callMenu ()