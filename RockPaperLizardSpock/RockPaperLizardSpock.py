# this is the classic game of rock paper scissors lizard spock as 
# originally mentioned in the sitcom big bang theory
# developing my own version as I am learning python

# code modules
import codemodule

#init variables
userselect = 0
userscore  = 0
computerscore = 0

while userselect != 9:
    #show the menu
    codemodule.showMenu()
    #get the user selection
    userselect = int(input())
    #check the selection and determine the action
    if(userselect not in range(1,6)):
        if (userselect == 9):
            print("Thanks for playing - Bye!")
            exit
        else:
            print("Invalid selection made! - Only enter 1 to 5")
    else:
        #get the computer selection
        computerselect = codemodule.computerSelects();
        #print the selections
        print("User selected:", codemodule.getSelectionName(int(userselect)))
        print("Computer selected:", codemodule.getSelectionName(int(computerselect)))
        #get the winner
        winner = codemodule.getWinner(userselect,computerselect )
        #print the winner
        if(winner!="stale"):
            print(winner, " Wins!")
        else:
            print(winner, " No one wins!")

        if (winner == "user"):
            userscore += 1
        elif (winner == "computer"):
            computerscore +=1
        #print the user score
        codemodule.printScore(userscore, computerscore)









