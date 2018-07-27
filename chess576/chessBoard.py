from chessConverters import str2num

class ChessBoard:
    def __init__(self):
        #example: myBoard.curr[1][4] is the piece at b5
        self.curr=[[0]*8 for i in range(8)] #pointers to piece, or 0=empty
        #first 01/ WB, second 01/allKing
        self.locations=[[[],[]] for i in range(2)]

    def reset(self): #is this doable through a reinitialization?
        self.curr=[[0]*8 for i in range(8)]
        self.locations=[[[],[]] for i in range(2)]

#makes deep copy for verifying legality of next move checks
    def copyBoard(self):
        clone = ChessBoard()
        for i in range(8):
            for j in range(8):
                clone.curr[i][j]=self.curr[i][j] #caution: SAME piece, NOT copy
        for i in range(2): # 0=White, 1=Black
            for j in range(2): #0=all positions, 1=just King(s)
                for x in self.locations[i][j]:
                    clone.locations[i][j].append(x)
        return clone

#gets piece at a given posiven
    def getSqr(self, pos):
        ind = str2num(pos)
        if ind==[]:
            print("Error: not a valid position")
            return
        return self.curr[ind[0]][ind[1]]

#empties out a square, does NOT update piece.pos (might be a ghost check)
    def delSqr(self, pos):
        ind = str2num(pos)
        if ind==[]:
            print("Error: not a valid position") #double print from str2num?
            return
        piece = self.getSqr(pos)
        if piece==0:
            # print("dest square is was empty") #test. prints on creation too
            return
        for i in range(2):
            if piece.pos in self.locations[piece.col][i]:
                self.locations[piece.col][i].remove(piece.pos)
        self.curr[ind[0]][ind[1]]=0

#sets board square to contain piece. does NOT update piece.pos (might be ghost)
    def setSqr(self, piece, dest):
        #below caused dependency cycle!
##        if not(isinstance(piece, ChessPiece)): #internal call. should be moot
##            print("Error: not a valid chess piece")
##            return
        ind = str2num(dest)
        if ind==[]:
            print("Error: not a valid position")
            return
        self.delSqr(piece.pos)
        self.delSqr(dest)
        self.locations[piece.col][0].append(dest)
        if piece.init=="K":
                self.locations[piece.col][1].append(dest)
        self.curr[ind[0]][ind[1]]=piece #this insures only cPiece (or 0) in curr