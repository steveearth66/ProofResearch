from chessBoard import ChessBoard

#for input scanning
colors = ["Black", "black", "White", "white"]
pieces = ["P", "R", "N", "B", "Q", "K"]

#move directions. 0=the four orthogonals, 1=four diagonals, 2=eight knight hops
vectors = [[],[],[]]
for x in range(-2,3):
    for y in range(-2, 3):
        if abs(x*y)==2:
            vectors[2].append([x,y])
        elif abs(x*y)==1:
            vectors[1].append([x,y])
        elif abs(x)+abs(y)==1:
            vectors[0].append([x,y])

board = ChessBoard()
next