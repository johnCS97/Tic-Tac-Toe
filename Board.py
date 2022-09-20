import numpy as np
from enum import Enum

class Player(Enum):
    empty=0
    AI=-2
    Person=2
    AIWin=-6
    PersonWin=6
    Draw=-1
    Playing=-2

class Board:
    def __init__(self):
        self.board_arr=np.zeros(shape=(3,3))
    
    def addMove(self,i,j,player):       
        self.board_arr[i][j]=player
        return check_winner(self.board_arr)

def check_winner(s):
        
        cols=np.sum(s,axis=0)
        rows=np.sum(s,axis=1)
        
        if Player.PersonWin.value in cols:
            return Player.PersonWin
        if Player.PersonWin.value in rows:
            return Player.PersonWin
        if Player.AIWin.value in cols:
            return Player.AIWin
        if Player.AIWin.value in rows:
            return Player.AIWin

        if np.trace(s)==Player.PersonWin.value:
            return Player.PersonWin
        if np.trace(s)==Player.AIWin.value:
            return Player.AIWin

        if np.sum(np.fliplr(s).diagonal())==Player.PersonWin.value:
            return Player.PersonWin
        if np.sum(np.fliplr(s).diagonal())==Player.AIWin.value:
            return Player.AIWin

        if Player.empty.value in s:
            return Player.Playing
        return Player.Draw