# Mastermind random choices
from random import sample, randint

def initGame():
    mylist = []
    myTwo = sample(range(7),2)
    initGuess = str(myTwo[0])+str(myTwo[0])+str(myTwo[1])+str(myTwo[1])
    if randint(0,1)%2==1:
        initGuess =str(myTwo[0])+str(myTwo[1])+str(myTwo[0])+str(myTwo[1])

    for q in [str(x) for x in range(7)]:
        for y in [str(x) for x in range(7)]:
            for z in [str(x) for x in range(7)]:
                for w in [str(x) for x in range(7)]:
                    mylist.append(q+y+z+w)
    return [mylist, initGuess]

def result(guess, sol):
    [black, white] = [0,0]
    for i in range(4):
        if guess[i] in sol:
            if guess[i]==sol[i]:
                black=black+1
            else:
                white=white+1
    return [black, white]

[mylist, currGuess] = initGame()
black=0
guess = 0
while black<4:
    guess = guess+1
    print("guess#"+str(guess)+" is "+currGuess)
    black = int(input("how many black pegs? "))
    white = int(input("how many white pegs? "))
    print(str(black)+" black, "+str(white)+" white")

    mylist = [s for s in mylist if result(currGuess, s)==[black,white]]
    if len(mylist)>0:
        currGuess = sample(mylist,1)[0]
    else:
        print("sorry, the answers you gave are inconsistent")
        black=4
print("Game ended after "+str(guess)+" guesses")