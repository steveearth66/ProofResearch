# unit testing for chess piece movements (no check checks yet)
# for CS576
# Author: Steve Earth, ver 1.5, 07/26/18

import unittest
from chessDriver import *

class TestStuff(unittest.TestCase):
    def test_pawn(self):
        x=ChessPiece("W", "P", "c5") #makes a white pawn at c5
        board.setSqr(x, "c5")
        self.assertEqual(x.moves(),['c6'])
        y=ChessPiece("W", "Q", "c6") #puts white queen in front of pawn
        board.setSqr(y, "c6")
        self.assertEqual(x.moves(),[])
        z=ChessPiece("B", "N", "b6")  #puts black knight diagonal of pawn
        board.setSqr(z, "b6")
        self.assertEqual(x.moves(),['b6'])
    def test_rook(self):
        board.reset();
        x,y,z=ChessPiece("W", "R", "c4"),ChessPiece("W", "Q", "c6"),\
        ChessPiece("B", "N", "f4")
        board.setSqr(x, "c4")
        board.setSqr(y, "c6")
        board.setSqr(z, "f4")
        self.assertEqual(x.moves(),\
        ['b4', 'a4', 'c3', 'c2', 'c1', 'c5', 'd4', 'e4', 'f4'])
    def test_bishop(self):
        board.reset();
        x,y,z=ChessPiece("W", "B", "c4"),ChessPiece("W", "Q", "a2"),\
        ChessPiece("B", "N", "e6")
        board.setSqr(x, "c4")
        board.setSqr(y, "a2")
        board.setSqr(z, "e6")
        self.assertEqual(x.moves(),['b3','b5','a6','d3','e2','f1','d5','e6'])
    def test_knight(self):
        board.reset();
        x,y,z=ChessPiece("W", "N", "d7"),ChessPiece("W", "Q", "f8"),\
        ChessPiece("B", "N", "e5")
        board.setSqr(x, "d7")
        board.setSqr(y, "f8")
        board.setSqr(z, "e5")
        self.assertEqual(x.moves(),['b6', 'b8', 'c5', 'e5', 'f6'])
    def test_queen(self):
        board.reset();
        x,y,z=ChessPiece("W", "Q", "c4"),ChessPiece("W", "P", "c2"),\
        ChessPiece("B", "N", "e4")
        board.setSqr(x, "c4")
        board.setSqr(y, "c2")
        board.setSqr(z, "e4")
        self.assertEqual(x.moves(),['b4','a4','c3','c5','c6','c7','c8','d4', \
        'e4','b3','a2','b5','a6','d3','e2','f1','d5','e6','f7','g8'])
    def test_king(self):
        board.reset();
        x,y,z=ChessPiece("W", "K", "d1"),ChessPiece("W", "Q", "e2"),\
        ChessPiece("B", "N", "c1")
        board.setSqr(x, "d1")
        board.setSqr(y, "e2")
        board.setSqr(z, "c1")
        self.assertEqual(x.moves(),['c1', 'd2', 'e1', 'c2'])

unittest.main()