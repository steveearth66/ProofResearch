from chessGlobals import board, vectors
from chessConverters import str2num, num2str

def ortho(myPiece): #for Rooks
    return genericMove(myPiece, 0, 8)

def diag(myPiece): #for Bishops
    return genericMove(myPiece, 1, 8)

def univ(myPiece): #for Queens
    return genericMove(myPiece,0,8)+genericMove(myPiece,1,8)

def oneStep(myPiece): #for King
    return genericMove(myPiece,0,2)+genericMove(myPiece,1,2)

def Lshape(myPiece): #for Knights
    return genericMove(myPiece,2,2)

def forward(myPiece): #dont need to pass whole piece, just color and pos
    [x,y] = str2num(myPiece.pos)
    # 1-2c makes white(0) move forward and black(1) move backwards
    poss=[[i,y+1-2*myPiece.col] for i in range(x-1,x+2)]
    ans = []
    for x in range(3):
        z =num2str(poss[x])
        if z=="":
            continue #this means off board, so skip to next possible square
        else:
            resident = board.getSqr(z)
            if x!=1: # this is a diagonal move
                #alternatively: could check if in Locations[myPiece.col]
                if resident==0 or resident.col==myPiece.col:
                    continue
                else:
                    ans.append(z) #enemy piece is diagonal to the pawn
            elif resident==0: #space in front empty
                ans.append(z)
    return ans

def genericMove(myPiece, j, rnge): #j=0/1=ortho/diag, rnge=2(single)/8(infinite)
    ans=[]
    [x,y] = str2num(myPiece.pos)
    for v in vectors[j]: #0 is horiz/vert, #1 diagonal
        #not strictly necessary, but saves + and * computation in next loop
        newx, newy  = x, y
##        print("checking direction: "+str(v))
        for i in range(1,rnge): #amt to increment, max is +7 steps
            newx += v[0] #could have done: newx =x+v[0]*i etc
            newy += v[1]
            z =num2str([newx,newy])
            if z=="":
##                print("off board, so changing direction")
                break #means off board; stop incrementing & go to next direction
            resident = board.getSqr(z)
            if resident==0: #destination square is empty
##                print(z+" is empty, so okay, keeping direction")
                ans.append(z)
            elif resident.col == myPiece.col:
##                print(z+" has teammate, not legal dest. change direction")
                break # blocked by teammate. try new direction
            else:
##                print(z+" has enemy, okay and change direction")
                ans.append(z) # would be a capture, and then new direction
                break
    return ans

moveType=[forward, ortho, Lshape, diag, univ, oneStep]