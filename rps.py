from prettytable import PrettyTable
import random

x1 = PrettyTable() #table that contains player streaks
x2 = PrettyTable() #table that contains scores after each round
x1.field_names = ["Round", "Your Streak", "Computer's Streak"]
x2.field_names = ["Your Score", "Computer's Score"]

def badInput(mine, choices): #function that handles bad input cases if input by the user. 
    print(f"\nYour input \"{mine}\" does not comply by the input cases.\nWanna try again?")
    yn = input("Type yes/y or no/n : ")
    c = 3 #no. of times the user is given an option to choose from the given choice of input. can be increased if need be.
    if yn == "yes" or yn == "y":
        while c > 0:
            print(f"\nRemaining chances --> {c}")
            inp = input("Go for it again!\nType R/r or P/p or S/s.\n")
            if inp in choices: return inp
            c -= 1
            if c == 0:
                print("\n\nBad input again!\nBye-Bye.\n")
                quit()

    elif yn == "no" or yn == "n":
        print("\n\nThankyou for holding up!\n")
        quit()
    else:
        print("\n\nBad input again!\nBye-Bye.\n")
        quit()


def inputs(mwins, cwins): #function that accepts input from the user, deals with case sensitivity and calls the function "badInput" if need be.
    mwins, cwins = mwins, cwins
    compChoice = random.choice(["r", "p", "s"])
    userChoices = ["r", "R", "p", "P", "s", "S"]
    myChoice = input("\nType R/r for \"rock\", P/p for \"paper\" and S/s for \"scissors\".\nChoose one : ")
    if myChoice not in userChoices:
        myChoice = badInput(myChoice, userChoices)
    if myChoice.isupper(): compChoice = compChoice.upper()
    else: compChoice = compChoice.lower()
    stat, mine, comps, res = singlePlay(myChoice, compChoice, mwins, cwins)
    #stat for "end statement", mine for "my score", comps for "computer score".
    #res = 1 if I win, -1 if I lose and 0 if we play a draw.
    return (stat, mine, comps, res)


def singlePlay(mine, comp, mwins, cwins): #function that randomly chooses a statement as per the win case and updates individual score
    tie = ["\n*** Your choice \"{}\" and the Computer's choice \"{}\" ends up in a Tie! ***\n", "\n*** Looks like Your \"{}\" and the Computer's \"{}\" is a Tie! ***\n", "\n*** {} vs {} means a Draw!.. Trying to match your Computer ehh? ***\n"]
    win = ["\n*** Your choice \"{}\" and the Computer's choice \"{}\" makes you the winner! ***\n", "\n*** Ahann.. Your choice \"{}\" makes you win against Computer's \"{}\". ***\n", "\n*** Very thoughtful of you to choose \"{}\"!.. You won against \"{}\". ***\n"]
    los = ["\n*** Pff.. these Computers! Your \"{}\" lost against \"{}\". ***\n", "\n*** OOPS!.. looks like Your \"{}\" lost against Computer's \"{}\". ***\n", "\n*** {} vs {}.. Hope you know what it means.. Sorry! ***\n"]
    if mine == comp:
        return (random.choice(tie).format(mine, comp), mwins, cwins, 0)
    if (mine.lower() == "r" and comp.lower() == "s") or (mine.lower() == "p" and comp.lower() == "r") or (mine.lower() == "s" and comp.lower() == "p"):
        mwins += 1
        return (random.choice(win).format(mine, comp), mwins, cwins, 1)
    cwins += 1
    return (random.choice(los).format(mine, comp), mwins, cwins, -1)


def bestOf(rounds, mwins, cwins): #the most vital function that handles the game. repeats the game until one of the players win. also renders the table we've been updating
    counter = 1
    while mwins < (rounds//2 + 1) and cwins < (rounds//2 + 1):
        stat, mine, comps, res= inputs(mwins, cwins)
        print(stat)
        mwins, cwins = mine, comps
        if res == 1: x1.add_row([counter, "Win", "Loss"])
        elif res == -1: x1.add_row([counter, "Loss", "Win"])
        else: x1.add_row([counter, "N/R", "N/R"])
        print(x1)
        counter += 1
        x2.add_row([mwins, cwins])
        print(x2)
        x2.clear_rows()
        print("\n")
    if mwins > cwins: print("\n\nCongratulations!.. You just won!.. What a Champ!\n\n")
    else: print("\n\nBetter luck next time buddy. You Computer's still smarter.\n\n")


if __name__ == "__main__": #the main driver code
    times = input("""\n\nHow many valid games do you wanna compete?
A game is valid only if we have a clear winner for the round.
Enter HERE : """)
    try:
        times = int(times)
    except:
        print("\n\nSorry!.. You just hit the wrong part of the keyboard.\n")
        quit()
    if times == 0:
        print("\n\nCool.. as you wish :(\n")
        quit()
    mwins, cwins = 0, 0
    bestOf(times, mwins, cwins)