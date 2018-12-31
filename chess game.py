import pygame
from random import randint
from math import pi
from math import sqrt

class ChessPiece:
    def __init__(self,pos_x = 0,pos_y = 0):
        print("S")
class PawnPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen,pos_x = 0,pos_y =  0, colour = (255,255,255)):
        pygame.draw.ellipse(screen, colour, (pos_x, pos_y-10, 20, 20))
        pygame.draw.rect(screen, colour, (pos_x+3.75, pos_y+20, 15, 25))
    @staticmethod
    def validMove(screen, pos_x = 0,pos_y = 0 ,state=0, board = [], colourMatrix = [], toPrint = True):
        potMove = []
        currentCol = colourMatrix[pos_y][pos_x]
        for i in range(1,3):
            if(state == 1):
                if(colourMatrix[pos_y - i][pos_x] != currentCol and not(pos_y - i < 0)):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * pos_x + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i, pos_x))
            elif(state == 2):
                if(colourMatrix[pos_y - i][pos_x] != currentCol and not(pos_y - i < 0)):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * pos_x + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i, pos_x))
                break
        if(not(pos_y - 1 < 0) and not (pos_x - 1 < 0)):
            if(colourMatrix[pos_y - 1][pos_x - 1] != currentCol and colourMatrix[pos_y - 1][pos_x - 1] != 0):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x-1) + 50, 87.5* (pos_y-1) + 50,88,88))
                potMove.append((pos_y-1,pos_x-1))
        if(not(pos_y - 1 < 0) and not (pos_x + 1 > 7)):
            if(colourMatrix[pos_y - 1][pos_x + 1] != currentCol and colourMatrix[pos_y - 1][pos_x + 1] != 0):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x+1) + 50, 87.5* (pos_y-1) + 50,88,88))
                potMove.append((pos_y-1,pos_x+1))
        potMove.append((pos_y, pos_x))
##        print(potMove)
        return potMove
class bPawnPiece(PawnPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        PawnPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen,pos_x = 0,pos_y =  0, colour = (255,255,255)):
        pygame.draw.ellipse(screen, colour, (pos_x, pos_y-10, 20, 20))
        pygame.draw.rect(screen, colour, (pos_x+3.75, pos_y+20, 15, 25))
    @staticmethod
    def validMove(screen, pos_x = 0,pos_y = 0, state=0, board = [], colourMatrix = [], toPrint = True):
        potMove = []
        currentCol = colourMatrix[pos_y][pos_x]
        for i in range(1,3):
            if(state == 1):
                if(colourMatrix[pos_y + i][pos_x] != currentCol and not(pos_y + i > 7)):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * pos_x + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x))
            elif(state == 2):
                if(colourMatrix[pos_y + i][pos_x] != currentCol and not(pos_y + i > 7)):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * pos_x + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x))
                break
        if(not(pos_y + 1 < 0) and not (pos_x - 1 < 0)):
            if(colourMatrix[pos_y + 1][pos_x - 1] != currentCol and colourMatrix[pos_y + 1][pos_x - 1] != 0):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x-1) + 50, 87.5* (pos_y+1) + 50,88,88))
                potMove.append((pos_y+1,pos_x-1))
        if(not(pos_y + 1 < 0) and not (pos_x + 1 > 7)):
            if(colourMatrix[pos_y + 1][pos_x + 1] != currentCol and colourMatrix[pos_y + 1][pos_x + 1] != 0):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x+1) + 50, 87.5* (pos_y+1) + 50,88,88))
                potMove.append((pos_y+1,pos_x+1))
        potMove.append((pos_y,pos_x))
        return potMove
class KnightPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen,pos_x = 0,pos_y =  0, colour = (255,255,255)):
        PawnPiece.create(screen,pos_x,pos_y, colour)
        pygame.draw.rect(screen, colour, (pos_x+3.75, pos_y+15, 15, 2))        
        pygame.draw.polygon(screen, colour, ((pos_x,pos_y),(pos_x-7,pos_y+5),(pos_x-7,pos_y+9),(pos_x+10,pos_y+9)))
        pygame.draw.polygon(screen, colour, ((pos_x+2,pos_y+21), (pos_x-5,pos_y+44), (pos_x+2,pos_y+44)))
        pygame.draw.polygon(screen, colour, ((pos_x+12,pos_y-10),(pos_x+25,pos_y-10),(pos_x+12,pos_y+5)))
    @staticmethod
    def validMove(screen, pos_x = 0,pos_y = 0, board = [], colourMatrix = [], toPrint = True):
        potMove = []
        currentCol = colourMatrix[pos_y][pos_x]
        for i in range(1,3):
            if((not pos_x - i < 0) and (not pos_y - (i) < 0)):
                if(colourMatrix[pos_y - (3-i)][pos_x - i] != currentCol):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x - i) + 50, 87.5* (pos_y - (3-i)) + 50,88,88))
                    potMove.append((pos_y - (3-i), pos_x - i))
            if((not pos_x + i > 7) and (not pos_y - (i) < 0)):
                if(colourMatrix[pos_y - (3-i)][pos_x + i] != currentCol):
                    if(toPrint):                    
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x + i) + 50, 87.5* (pos_y - (3-i)) + 50,88,88))
                    potMove.append((pos_y - (3-i), pos_x + i))
            if((not pos_x - i < 0) and (not pos_y + (i) > 7)):
                if(colourMatrix[pos_y + (3-i)][pos_x - i] != currentCol):
                    if(toPrint):                    
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x - i) + 50, 87.5* (pos_y + (3-i)) + 50,88,88))
                    potMove.append((pos_y + (3-i), pos_x - i))
            if((not pos_x + i > 7 ) and (not pos_y + (i) > 7)):
                if(colourMatrix[pos_y + (3-i)][pos_x + i] != currentCol):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x + i) + 50, 87.5* (pos_y + (3-i)) + 50,88,88))
                    potMove.append((pos_y + (3-i), pos_x + i))
        potMove.append((pos_y,pos_x))
        return potMove

class BishopPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen, pos_x = 0, pos_y = 0, colour = (255,255,255)):
        PawnPiece.create(screen,pos_x,pos_y, colour)
        pygame.draw.arc(screen, colour, (pos_x-2,pos_y-31,25,40),3*pi/2,pi/2,3)
        pygame.draw.arc(screen, colour, (pos_x-2,pos_y-31,25,40),3*pi/4,2*pi,3)
    
    def validMove(screen, pos_x = 0,pos_y = 0,board = [], colourMatrix = [], toPrint = True):
        potMove = []
        currentCol = colourMatrix[pos_y][pos_x]
        state = [0,0,0,0]
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0) and (not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x - i] == currentCol or state[0] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x - i) + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x-i))
                    if(colourMatrix[pos_y - i][pos_x - i] != currentCol and colourMatrix[pos_y - i][pos_x - i] != 0):
                        state[0] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7) and (not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x + i] == currentCol or state[1] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x + i) + 50, 87.5* (pos_y - i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x+i))
                    if(colourMatrix[pos_y - i][pos_x + i] != currentCol and colourMatrix[pos_y - i][pos_x + i] != 0):
                        state[1] = 1
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0) and (not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x - i] == currentCol or state[2] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x - i) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x-i))
                    if(colourMatrix[pos_y + i][pos_x - i] != currentCol and colourMatrix[pos_y + i][pos_x - i] != 0):
                        state[2] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7) and (not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x + i] == currentCol or state[3] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x + i) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x+i))
                    if(colourMatrix[pos_y + i][pos_x + i] != currentCol and colourMatrix[pos_y + i][pos_x + i] != 0):
                        state[3] = 1
        potMove.append((pos_y,pos_x))
        return potMove
class RookPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen, pos_x = 0, pos_y = 0, colour = (255,255,255)):
        pygame.draw.rect(screen, colour, (pos_x+3.75, pos_y+20, 15, 25))
        pygame.draw.rect(screen, colour, (pos_x-5,pos_y+30, 30, 15))
        pygame.draw.rect(screen, colour, (pos_x, pos_y, 20, 5))
    def validMove(screen, pos_x = 0,pos_y = 0,board = [],colourMatrix = [],toPrint = True):
        potMove = [] 
        currentCol = colourMatrix[pos_y][pos_x]
        bstate = [0,0,0,0]
        for i in range(1,pos_y+1):
            if((not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x] == currentCol or bstate[0] == 1):
                    break
                else:
                    if(toPrint):                    
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x) + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x))
                    if(colourMatrix[pos_y - i][pos_x] != currentCol and colourMatrix[pos_y - i][pos_x] != 0):
                        bstate[0] = 1
        for i in range(1,8-pos_y):
            if((not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x] == currentCol or bstate[1] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x))
                    if(colourMatrix[pos_y + i][pos_x] != currentCol and colourMatrix[pos_y + i][pos_x] != 0):
                        bstate[1] = 1
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0)):
                if(colourMatrix[pos_y][pos_x - i] == currentCol or bstate[2] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x-i) + 50, 87.5* (pos_y) + 50,88,88))
                    potMove.append((pos_y,pos_x-i))
                    if(colourMatrix[pos_y][pos_x - i] != currentCol and colourMatrix[pos_y][pos_x - i] != 0):
                        bstate[2] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7)):
                if(colourMatrix[pos_y][pos_x + i] == currentCol or bstate[3] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x+i) + 50, 87.5* (pos_y) + 50,88,88))
                    potMove.append((pos_y,pos_x+i))
                    if(colourMatrix[pos_y][pos_x + i] != currentCol and colourMatrix[pos_y][pos_x + i] != 0):
                        bstate[3] = 1
        potMove.append((pos_y,pos_x))
        return potMove

class QueenPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen, pos_x = 0, pos_y = 0, colour = (255,255,255)):
        pygame.draw.rect(screen, colour, (pos_x+3.75, pos_y+5, 10, 40))
        pygame.draw.polygon(screen, colour, ((pos_x+3.75, pos_y),(pos_x+13.74, pos_y),(pos_x+8.75,pos_y-5)))
    def validMove(screen, pos_x = 0,pos_y = 0, board = [], colourMatrix = [], toPrint = True):
        potMove = [] 
        currentCol = colourMatrix[pos_y][pos_x]
        state = [0,0,0,0]
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0) and (not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x - i] == currentCol or state[0] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x - i) + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x-i))
                    if(colourMatrix[pos_y - i][pos_x - i] != currentCol and colourMatrix[pos_y - i][pos_x - i] != 0):
                        state[0] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7) and (not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x + i] == currentCol or state[1] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x + i) + 50, 87.5* (pos_y - i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x+i))
                    if(colourMatrix[pos_y - i][pos_x + i] != currentCol and colourMatrix[pos_y - i][pos_x + i] != 0):
                        state[1] = 1
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0) and (not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x - i] == currentCol or state[2] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x - i) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x-i))
                    if(colourMatrix[pos_y + i][pos_x - i] != currentCol and colourMatrix[pos_y + i][pos_x - i] != 0):
                        state[2] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7) and (not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x + i] == currentCol or state[3] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x + i) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x+i))
                    if(colourMatrix[pos_y + i][pos_x + i] != currentCol and colourMatrix[pos_y + i][pos_x + i] != 0):
                        state[3] = 1
        bstate = [0,0,0,0]
        for i in range(1,pos_y+1):
            if((not pos_y - i < 0)):
                if(colourMatrix[pos_y - i][pos_x] == currentCol or bstate[0] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x) + 50, 87.5* (pos_y-i) + 50,88,88))
                    potMove.append((pos_y-i,pos_x))
                    if(colourMatrix[pos_y - i][pos_x] != currentCol and colourMatrix[pos_y - i][pos_x] != 0):
                        bstate[0] = 1
        for i in range(1,8-pos_y):
            if((not pos_y + i > 7)):
                if(colourMatrix[pos_y + i][pos_x] == currentCol or bstate[1] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x) + 50, 87.5* (pos_y+i) + 50,88,88))
                    potMove.append((pos_y+i,pos_x))
                    if(colourMatrix[pos_y + i][pos_x] != currentCol and colourMatrix[pos_y + i][pos_x] != 0):
                        bstate[1] = 1
        for i in range(1,pos_x+1):
            if((not pos_x - i < 0)):
                if(colourMatrix[pos_y][pos_x - i] == currentCol or bstate[2] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x-i) + 50, 87.5* (pos_y) + 50,88,88))
                    potMove.append((pos_y,pos_x-i))
                    if(colourMatrix[pos_y][pos_x - i] != currentCol and colourMatrix[pos_y][pos_x - i] != 0):
                        bstate[2] = 1
        for i in range(1,8-pos_x):
            if((not pos_x + i > 7)):
                if(colourMatrix[pos_y][pos_x + i] == currentCol or bstate[3] == 1):
                    break
                else:
                    if(toPrint):
                        pygame.draw.rect(screen, (1,55.5,1.5), (87.5 * (pos_x+i) + 50, 87.5* (pos_y) + 50,88,88))
                    potMove.append((pos_y,pos_x+i))
                    if(colourMatrix[pos_y][pos_x + i] != currentCol and colourMatrix[pos_y][pos_x + i] != 0):
                        bstate[3] = 1
        potMove.append((pos_y,pos_x))
##        print("POT",potMove)
        return potMove


class KingPiece(ChessPiece):
    def __init__(self,pos_x = 0,pos_y = 0):
        ChessPiece.__init__(self,pos_x,pos_y)
    @staticmethod
    def create(screen, pos_x = 0, pos_y = 0, colour = (255,255,255)):
        pygame.draw.rect(screen, colour, (pos_x, pos_y+5, 20, 40))
        pygame.draw.polygon(screen, colour, ((pos_x, pos_y-5),(pos_x+20, pos_y-5),(pos_x+8.75,pos_y)))
    def validMove(screen, pos_x = 0,pos_y = 0, board = [], colourMatrix = [], influence = [], colour = "w", toPrint = True):
        potMove = []
        currentCol = colourMatrix[pos_y][pos_x]
        for i in range(0,3):
            if((not pos_x-1 + i > 7) and (not pos_y - 1 < 0) and (not pos_x-1 + i < 0)):
                if(colourMatrix[pos_y-1][pos_x-1 + i] != currentCol and not loopCheck((pos_y - 1, pos_x -1 + i), colourMatrix, currentCol, influence) and board[pos_y-1][pos_x-1+i] != currentCol):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x-1 + i) + 50, 87.5* (pos_y-1) + 50,88,88))
##                    print((pos_y-1,pos_x-1+i),"0")
                    potMove.append((pos_y-1,pos_x-1+i))
            if((not pos_x-1 + i > 7) and (not pos_y + 1 > 7) and (not pos_x-1 + i < 0)):
##                print((pos_y + 1, pos_x -1 + i),loopCheck((pos_y + 1, pos_x -1 + i), colourMatrix,  currentCol, influence), "SS")
                if(colourMatrix[pos_y+1][pos_x-1 + i] != currentCol and not loopCheck((pos_y + 1, pos_x -1 + i), colourMatrix,  currentCol, influence) and board[pos_y+1][pos_x-1+i] != currentCol):
                    if(toPrint):
                        pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x-1 + i) + 50, 87.5* (pos_y+1) + 50,88,88))
##                    print((pos_y+1,pos_x-1+i),"1")
                    potMove.append((pos_y+1,pos_x-1+i))
        if((not pos_x-1 < 0) and (not pos_y < 0) and (not pos_y > 7 )):
            if(colourMatrix[pos_y][pos_x-1] != currentCol and not loopCheck((pos_y, pos_x -1), colourMatrix, currentCol,  influence) and board[pos_y][pos_x-1] != currentCol):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x-1) + 50, 87.5* (pos_y) + 50,88,88))
##                print((pos_y,pos_x-1),"2")
                potMove.append((pos_y,pos_x-1))
        if((not pos_x+1 > 7) and (not pos_y < 0) and (not pos_y > 7)):
            if(colourMatrix[pos_y][pos_x+1] != currentCol and (not loopCheck((pos_y, pos_x + 1), colourMatrix,  currentCol, influence) and board[pos_y][pos_x+1] != currentCol)):
                if(toPrint):
                    pygame.draw.rect(screen,(1,55.5,1.5),(87.5 * (pos_x+1) + 50, 87.5* (pos_y) + 50,88,88))
##                print((pos_y,pos_x+1),"3")
                potMove.append((pos_y,pos_x+1))
        potMove.append((pos_y,pos_x))
##        print(potMove)
        return potMove
def loadBoard(board,screen, colourMatrix):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] != 0):
                if(colourMatrix[i][j] == "b"):
                    board[i][j].create(screen,87.5*j + 85 ,87.5*i + 88, (200,200,200))
                else:
                    board[i][j].create(screen,87.5*j + 85 ,87.5*i + 88)
def loadTile(board,screen):
    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(screen,(2,111,3),(87.5 * j + 50, 87.5* i + 50,88,88))
def checkKingCheck(colour, screen, colourMatrix, board, pawnMatrix):
    influence = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(colourMatrix[i][j] != colour and board[i][j] != KingPiece  and board[i][j] != 0):
                if(board[i][j] == PawnPiece or board[i][j] == bPawnPiece):
                    influence.append(board[i][j].validMove(screen,j,i, pawnMatrix[i][j], board, colourMatrix, False))
                else:
                    influence.append(board[i][j].validMove(screen,j,i, board, colourMatrix, False))
    return influence
def loopCheck(tup, colourMatrix, colour, influence):
##    print(influence, "SSS")
    for i in range(len(influence)):
        for j in range(len(influence[i])):
##            print(influence[i][j], tup)
            if(influence[i][j] == tup):
                return True
    return False
def main():
    pygame.init()
    board = [[RookPiece, KnightPiece, BishopPiece, QueenPiece, KingPiece, BishopPiece, KnightPiece, RookPiece],
             [bPawnPiece, bPawnPiece, bPawnPiece, bPawnPiece, bPawnPiece, bPawnPiece, bPawnPiece, bPawnPiece],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [PawnPiece, PawnPiece, PawnPiece, PawnPiece, PawnPiece, PawnPiece, PawnPiece, PawnPiece],
             [RookPiece, KnightPiece, BishopPiece, KingPiece, QueenPiece, BishopPiece, KnightPiece, RookPiece]]
    pawnMatrix = [[0,0,0,0,0,0,0,0],
                  [1,1,1,1,1,1,1,1],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [1,1,1,1,1,1,1,1],
                  [0,0,0,0,0,0,0,0]]
    colourMatrix = [["b","b","b","b","b","b","b","b"],
                    ["b","b","b","b","b","b","b","b"],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    ["w","w","w","w","w","w","w","w"],
                    ["w","w","w","w","w","w","w","w"]]
    screen = pygame.display.set_mode((800,800))
    screen.fill((110,0,00))
    loadBoard(board,screen, colourMatrix)
    pygame.draw.rect(screen,(255,255,255), (50,50,700,700),1)
    pygame.display.update()
    clickState = False
    currentPiece = 0
    currentPos = (0,0)
    currentCol = 0
    colourCounter = "w"
    turnComplete = False    
    bKingPos = (4,0)
    wKingPos = (7,3)
    potMove = (-1,-1)
    kPotMove = 0
    binCheck = False
    winCheck = False
    while True:
        screen.fill((110,0,0))
        loadTile(board,screen)
        loadBoard(board,screen, colourMatrix)
        pygame.draw.rect(screen,(255,255,255), (50,50,700,700),1)
        influence = checkKingCheck(colourCounter, screen, colourMatrix, board, pawnMatrix)
        if(colourCounter == "b"):
            print(checkKingCheck("b", screen, colourMatrix, board, pawnMatrix), "start")
            print(bKingPos[1],bKingPos[0])
            if(loopCheck((bKingPos[1],bKingPos[0]), colourMatrix, colourCounter,checkKingCheck("b", screen, colourMatrix, board, pawnMatrix))):
                binCheck = True
                print("Black in Check")
            else:
                binCheck = False
        elif(colourCounter == "w"):
            if(loopCheck((wKingPos[0],wKingPos[1]), colourMatrix,  colourCounter, checkKingCheck("w", screen, colourMatrix, board, pawnMatrix))):
                winCheck = True
                print("White in Check")
            else:
                winCheck = False
        if(clickState and currentPiece != 0):
            screen.fill((110,0,0))
            loadTile(board,screen)
            if(clickState):
                if(currentPiece == PawnPiece or currentPiece == bPawnPiece):
                    potMove = currentPiece.validMove(screen,currentPos[0],currentPos[1],pawnMatrix[currentPos[1]][currentPos[0]],board, colourMatrix)
                elif(currentPiece == KingPiece):
                    potMove = currentPiece.validMove(screen,currentPos[0],currentPos[1],board, colourMatrix, influence, colourCounter)
                else:
                    potMove = currentPiece.validMove(screen,currentPos[0],currentPos[1],board, colourMatrix)
            loadBoard(board,screen, colourMatrix)
            pygame.draw.rect(screen,(255,255,255), (50,50,700,700),1)
            if(colourMatrix[currentPos[1]][currentPos[0]] == "b"):
                currentPiece.create(screen,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], (200,200,200))
            else:
                currentPiece.create(screen,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        pygame.display.update()
        if(colourCounter == "w"):
            kPotMove = KingPiece.validMove(screen,wKingPos[0],wKingPos[1],board, colourMatrix, influence,colourCounter, False)
        else:
            kPotMove = KingPiece.validMove(screen,bKingPos[1],bKingPos[0],board, colourMatrix, influence,colourCounter, False)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(board)):
                        for j in range(len(board[i])):
                            if(pygame.mouse.get_pos()[0] > 50 + 88*(j) and pygame.mouse.get_pos()[0] < 750 and pygame.mouse.get_pos()[1] > 50 + 88*(i) and pygame.mouse.get_pos()[1] < 750):
                                if(pygame.mouse.get_pos()[0] < 50 + 88*(j+1) and pygame.mouse.get_pos()[1] < 50 + 88*(i+1)):
                                    if(colourMatrix[i][j] != colourCounter and clickState and (i,j) in potMove or (i == currentPos[1] and j == currentPos[0] and clickState and (i,j) in potMove)):
                                        board[i][j] = currentPiece
                                        if(i == currentPos[1] and j == currentPos[0]):
                                            currentPiece = 0
                                            clickState = False
                                            break                                            
                                        if(currentPiece == PawnPiece or currentPiece == bPawnPiece):
                                            pawnMatrix[currentPos[1]][currentPos[0]] = 0
                                            pawnMatrix[i][j] = 2
                                        colourMatrix[currentPos[1]][currentPos[0]] = 0
                                        colourMatrix[i][j] = colourCounter
                                        clickState = False
                                        currentPos = (j,i)
                                        if(currentPiece == KingPiece):
                                            if(colourCounter == "w"):
                                                wKingPos = (currentPos[1],currentPos[0])
                                            elif(colourCounter == "b"):
                                                bKingPos = (currentPos[1],currentPos[0])
                                        turnComplete = True
                                        currentPiece = 0
                                        break
                                    if(not clickState and colourCounter == colourMatrix[i][j]):
                                        clickState = True
                                        currentPiece = board[i][j]
                                        currentPos = (j,i)
                                        currentCol = colourMatrix[i][j]
                                        board[i][j] = 0
                                        break
                if event.type == pygame.QUIT:
                    exit()
            break
        if(turnComplete):
            if(colourCounter == "w"):
                colourCounter = "b"
            else:
                colourCounter = "w"
            turnComplete = False

main()
