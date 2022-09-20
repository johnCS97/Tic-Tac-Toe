import Board as bd
from Board import Player 
import numpy as np
def minimax(board,player):
    bestscore=0
    if(player==Player.AI):
        bestscore=-1
    if(player==Player.Person):
        bestscore=1
    
    x=0
    y=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                
                board[i][j]=player.value
                status=bd.check_winner(board)
                if(status==Player.Draw):
                    board[i][j]==0
                    
                    return 0,i,j
                if(status==Player.PersonWin):
                    board[i][j]==0
                    
                    return -1,i,j
                if(status==Player.AIWin):
                    board[i][j]==0
                    
                    return 1,i,j
                tempBoard=np.copy(board)
                if(player==Player.Person):
                    s,t,m=minimax(tempBoard,Player.AI)
                else:
                    s,t,m=minimax(tempBoard,Player.Person)

                
                if(s>bestscore and player==Player.AI):
                    bestscore=s
                    x,y=i,j
                if(s<bestscore and player==Player.Person):
                    bestscore=s
                    x,y=i,j
                board[i][j]=0
    return bestscore,x,y
                
