import random

def badInput(mine, choices):
    print(f"\nYour input \"{mine}\" does not comply by the input cases.\nWanna try again?")
    yn = input("Type yes/y or no/n : ")
    c = 3
    if yn == "yes" or yn == "y":
        while c > 0:
            print(f"\nRemaining chances --> {c}")
            inp = input("Go for it again!\nType R/r or P/p or S/s.\n")
            if inp in choices: return inp
            c -= 1
            if c == 0:
                print("\nBad input again!\nBye-Bye.\n")
                quit()

    elif yn == "no" or yn == "n":
        print("Thankyou for holding up!")
        quit()
    else:
        print("\nBad input again!\nBye-Bye.\n")
        quit()


def inputs(mwins, cwins):
    mwins, cwins = mwins, cwins
    compChoice = random.choice(["r", "p", "s"])
    userChoices = ["r", "R", "p", "P", "s", "S"]
    myChoice = input("\nType R/r for \"rock\", P/p for \"paper\" and S/s for \"scissors\".\nChoose one : ")
    if myChoice not in userChoices:
        myChoice = badInput(myChoice, userChoices)
    if myChoice.isupper(): compChoice = compChoice.upper()
    else: compChoice = compChoice.lower()
    stat, mine, comps = singlePlay(myChoice, compChoice, mwins, cwins)
    return (stat, mine, comps)


def singlePlay(mine, comp, mwins, cwins):
    tie = ["\n*** Your choice \"{}\" and the Computer's choice \"{}\" ends up in a Tie! ***\n", "\n*** Looks like Your \"{}\" and the Computer's \"{}\" is a Tie! ***\n", "\n*** {} vs {} means a Draw!.. Trying to match your Computer ehh? ***\n"]
    win = ["\n*** Your choice \"{}\" and the Computer's choice \"{}\" makes you the winner! ***\n", "\n*** Ahann.. Your choice \"{}\" makes you win against Computer's \"{}\". ***\n", "\n*** Very thoughtful of you to choose \"{}\"!.. You won against \"{}\". ***\n"]
    los = ["\n*** Pff.. these Computers! Your \"{}\" lost against \"{}\". ***\n", "\n*** OOPS!.. looks like Your \"{}\" lost against Computer's \"{}\". ***\n", "\n*** {} vs {}.. Hope you know what it means.. Sorry! ***\n"]
    if mine == comp:
        return (random.choice(tie).format(mine, comp), mwins, cwins)
    if (mine.lower() == "r" and comp.lower() == "s") or (mine.lower() == "p" and comp.lower() == "r") or (mine.lower() == "s" and comp.lower() == "p"):
        mwins += 1
        return (random.choice(win).format(mine, comp), mwins, cwins)
    cwins += 1
    return (random.choice(los).format(mine, comp), mwins, cwins)


def bestOf(rounds, mwins, cwins):
    while mwins < (rounds//2 + 1) and cwins < (rounds//2 + 1):
        stat, mine, comps = inputs(mwins, cwins)
        print(stat)
        mwins, cwins = mine, comps
        print(f"Your wins : {mwins}   Comp wins : {cwins}")
    if mwins > cwins: print("Congratulations!.. You just won!.. What a Champ!")
    else: print("Better luck next time buddy. You Computer's still smarter.")


if __name__ == "__main__":
    times = int(input("\nHow many rounds do you wanna compete? : "))
    if times == 0:
        print("Cool.. as you wish :(")
        quit()
    mwins, cwins = 0, 0
    bestOf(times, mwins, cwins)