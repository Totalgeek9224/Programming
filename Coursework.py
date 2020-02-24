print('''\  
  _______ __      ______              ______         
 /_  __(_) /__   /_  __/___ ______   /_  __/___  ___ 
  / / / / //_/    / / / __ `/ ___/    / / / __ \/ _ \\
 / / / / ,<      / / / /_/ / /__     / / / /_/ /  __/
/_/ /_/_/|_|    /_/  \__,_/\___/    /_/  \____/\___/     

                  By Zachary DeMarco                 
                                                
                                                             ''')
#
##########################
### Declare Statements ###
##########################

userInitials = []


################
### Functions ###
################

# Funtion to collect user Initials, preventing numbers, while also confirming user intitals before proceeding.
# Additionally, 
def collectInitials ():

    # Ask user for Initials
    userInitials = input('Enter your 3 initials: ')
    if userInitials == ("quit" or "Quit"):
        quit()

    # Confirm only letters
    while (userInitials.isalpha() == False) or not (len(userInitials) == 3):
        print('Incorrect Formatting- Please try again')
        userInitials = input('Enter your 3 initials: ')
        if userInitials == ("quit" or "Quit"):
            quit()

    print ("Your initials are:" + userInitials.upper())

    
#################
### Main Code ###
#################

collectInitials ()

