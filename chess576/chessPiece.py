from chessConverters import str2num, num2str
from chessMoves import moveType
from chessGlobals import pieces

class ChessPiece:
    def __init__(self, clr, pType, xy):
        if pType not in pieces:
            print("Error: not a piece type")
            self.init="X"
        else:
            self.init = pType
        # 0 is for a White piece, 1 is for a Black piece (default = 0)
        if not(isinstance(clr, str)) or clr=="" or clr[0].lower()!="b":
            self.col = 0
        else:
            self.col=1
        ind = str2num(str(xy)) #only need to convert to str for testing
        self.pos = num2str(ind)
        if ind==[]:
            print("invalid position for "+self.col+" "+self.init)

    def __str__(self):
        return ["White", "Black"][self.col]+" "+self.init+self.pos
    def moves(self):
        return moveType[pieces.index(self.init)](self)