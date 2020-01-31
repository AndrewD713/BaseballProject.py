# Author:  Andrew Davidson
# Date:    04/10/2019
# 
# This application tracks baseball players batting average using parallel lists.
# The user can enter 12 player names, which are then populated into a list.
# The user can switch between name entry, stat entry, and summary display during runtime. name entry allows
# the user to enter 12 player names. Stat entry allows the user to enter player number, at bats, and hits. 
# Display summary will display the player names, at bats, hits, and average.

import os

clear = lambda : os.system('cls')
listNames = list()
listBats = list()
listHits = list()

def main():
    init()
    menu()

def init():
    #initializes 12 default slots in the parallel lists
    for x in range(12):
        listNames.append("")
        listBats.append(0)
        listHits.append(0)

def menu():
    #Calls function based on option selected
    optionSelect = 0
    
    clear()
    print("Please select an option")
    
    optionSelect = optionInputAndValidation()

    if optionSelect == 1:
        optionEnterNames()
    elif optionSelect == 2:
        optionEnterStats()
    elif optionSelect == 3:
        optionDisplaySummary()
    else: 
        clear()
        print("Program ending...")


def optionInputAndValidation():
    #Prompts user to enter 1-4. Loops until valid option is entered.
    option = 0
    errSw = True

    while errSw:
        print("1 - Enter Player Names")
        print("2 - Enter Player Stats")
        print("3 - Display Summary")
        print("4 - Exit Program")
        try:
            option = int(input())
            if option < 1 or option > 4:
                print("\nInvalid option. Please select 1-4")
            else:
                errSw = False
        except:
            print("\nInvalid option. Please select 1-4")

    return option

def optionEnterNames():
    #Prompts user to enter in 12 player names. Validates to make sure name is not empty. Places names into listNames
    #returns to main menu once completed
    clear()
    for x in range(12):
        print("Enter a name for player #", x + 1)
        playerName = str(input())

        while not playerName:
            print("\nInvalid player name. Player name cannot be empty.")
            print("Enter a name for player #", x + 1)
            playerName = str(input())
            
        listNames[x] = playerName

    print("\n\nPlayer names entered sucessfully.")
    print("Press enter to return to main menu...")
    input()
    menu()

def optionEnterStats():
    #Calls functions to prompt for data entry. Validates that hits do not exceed bats.
    #Loops while user wants to enter more data.
    errSw = True
    playerNum = 0
    bats = 0
    hits = 0
    again = "y"

    while again == "y" or again == "Y":
        clear()
        errSw = True

        while errSw:
            playerNum = playerNumInputAndValidation()
            bats = batsInputAndValidation()
            hits = hitsInputAndValidation()

            if hits > bats:
                print("\nError! Hits can't be greater than At Bats. Please re-enter data.")
            else:
                errSw = False

        #Places data entered into appropriate places on lists based on player number
        listHits[playerNum - 1] += hits
        listBats[playerNum - 1] += bats

        #Asks user if they want to enter more data
        print("Data submitted! Would you like to enter more data? (Y/N)");
        again = input()

    menu()

def playerNumInputAndValidation():
    p = 0
    errSw = True

    #Prompts user to enter player number (1-12). Loops until valid.
    while errSw:
        try:
            p = int(input("Enter Player Number (1-12):\n"))
            if p < 1 or p > 12:
                print("\nInvalid Player Number. Please enter 1-12.")
            else:
                errSw = False
        except:
            print("\nInvalid Player Number. Please enter 1-12.")

    return p

def batsInputAndValidation():
    b = 0
    errSw = True

    #Prompts the user to enter "at bats" for their entered player. Loops until valid.
    while errSw:
        try:
            b = int(input("Enter number of At Bats:\n"))
            if b < 0:
                print("\nInvalid At Bats. Please enter a whole number.")
            else:
                errSw = False
        except:
            print("\nInvalid At Bats. Please enter a whole number.")

    return b

def hitsInputAndValidation():
    h = 0
    errSw = True

    #Prompts the user to enter hits for their entered player. Loops until valid.
    while errSw:
        try:
            h = int(input("Enter number of Hits:\n"))
            if h < 0:
                print("\nInvalid Hits. Please enter a whole number.")
            else:
                errSw = False
        except:
            print("\nInvalid Hits. Please enter a whole number.")

    return h

def optionDisplaySummary():
    avg = 0.0

    clear()
    #Header
    print("-------------------------------------------")
    print("{0:16s} | {1:7s} | {2:4s} | {3:7s}".format("Player Name", "At Bats", "Hits", "Average"))
    print("-------------------------------------------")

    #Calls method to calculate average (passing x), and then formats / prints summary report.
    for x in range(12):
        avg = calcAvg(x)
        print("{0:16s} | {1:7d} | {2:4d} | {3:7.3f}".format(listNames[x], listBats[x], listHits[x], avg))

    print("\nPress Enter to return to main menu...");
    input()
    menu();

def calcAvg(x):
    #Calculates batting average for player. If hits are 0, then returns 0 to avoid division by 0.
    if listHits[x] == 0:
        return 0
    else:
        return 1.0 * listHits[x] / listBats[x]

main()