import random

rockbeats = tuple((3, 4))
paperbeats = tuple((1,5 ))
scissorsbeats = tuple((2, 4))
lizardbeats = tuple((2,5))
spockbeats= tuple((1, 3))

def showMenu():
    print("What do you choose - Enter a selection 1 to 5")
    print("=========================================================")
    print("1. Rock - 2. Paper - 3. Scissors - 4. Lizard - 5. Spock")
    print("9 to Quit!")
    print("=========================================================")

def computerSelects():
    r= random.randint(1, 5)
    #print(r)
    return r


def getSelectionName(nsel):
    if(nsel==1):
        return "Rock"
    elif(nsel==2):
        return "Paper"
    elif(nsel==3):
        return "Scissors"
    elif(nsel==4):
        return "Lizard"
    elif(nsel==5):
        return "Spock"
    

def getWinner(user, comp):
    if (user == comp):
        winner = "stale"
    elif (user == 1):
        if (comp in rockbeats):
            winner = "user"
        else:
            winner = "computer"
    elif (user == 2):
        if (comp in paperbeats):
            winner = "user"
        else:
            winner = "computer"
    elif (user == 3):
        if (comp in scissorsbeats):
            winner = "user"
        else:
            winner = "computer"
    elif (user == 4):
        if (comp in lizardbeats):
            winner = "user"
        else:
            winner = "computer"
    elif (user == 5):
        if (comp in spockbeats):
            winner = "user"
        else:
            winner = "computer"
    return winner

def printScore(user, comp):
    print ("**USER WINS**[",user, "]**COMPUTER WINS**[",comp,"]")

