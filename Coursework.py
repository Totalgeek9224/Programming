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
    # Quit sequence to allow quit from any stage of the program
    userPanic = False
    if  == ["quit", "Quit", "QUIT"]:
        userPanic = True

    while userPanic == False:

        (correctInnitials) = False

        while correctInnitials == False:

            # Ask user for Initials
            userInitials = input('Enter your initials: ')

            #Confirm only letters
            while (userInitials.isalpha() == False):
                print('Letters only, please')
                userInitials = input('Enter your initials: ')

            # Confirm user initials, ending the collectInitials Function
            print (userInitials.upper())
            userConfirm = input ('Are these correct? Y/N ')

            while (userConfirm not in ["Y","N", "y", "n"]):
                print ('Input not recognised - try again')
                userConfirm = input ('Are these correct? Y/N ')

            if (userConfirm == 'Y' or userConfirm == 'y'):
                correctInnitials = True


#################
### Main Code ###
#################

collectInitials ()
print(userInitials)

