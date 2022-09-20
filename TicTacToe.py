from calendar import c
from re import M
from turtle import st
import Board as bd
import pygame as pg
import Input
import sys
import time
from pygame.locals import *
import numpy as np
import AI


from Board import Player

pg.init()

fps=30

line_color = (0, 0, 0)

white = (255, 255, 255)

board = [[None]*3, [None]*3, [None]*3]

clock=pg.time.Clock()

width=400
height=400

screen=pg.display.set_mode((width, height + 100), 0, 32)

boardgame=bd.Board()

initiating_window = pg.image.load("modified_cover.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("O_modified.png")

initiating_window = pg.transform.scale(initiating_window, (width, height))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

def game_initiating_window():
    
    # displaying over the screen
     
    # updating the display
    pg.display.update()
    # time.sleep(3)                   
    screen.fill(white)
  
    # drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
  
    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    # draw_status()

font = pg.font.Font(None, 30)

PlayerTurn=Player.AI
if __name__ == "__main__":
   game_initiating_window()
   text = font.render(PlayerTurn.name, 1, (255, 255, 255))
   text_rect = text.get_rect(center =(width / 2, 500-50))
   screen.blit(text, text_rect)
   while(True):
    if(PlayerTurn==Player.Draw or PlayerTurn==Player.AIWin or PlayerTurn==Player.PersonWin):
        text = font.render("Play Again", 1, (255, 255, 255))
        text_rect = text.get_rect(center =(width / 4, 500-50))
        screen.blit(text, text_rect)
        if(event.type == MOUSEBUTTONDOWN):
            mouse=pg.mouse.get_pos()
            if(mouse[0]>(width / 4)-60 and mouse[0]<(width / 4)+60):
                if(mouse[1]>(500-50)-10 and mouse[1]<(500-50)+10):
                    PlayerTurn=Player.AI

                    screen.fill(white)
                    

                     # drawing vertical lines
                    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
                    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
                    # drawing horizontal lines
                    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
                    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
                    screen.fill ((0, 0, 0), (0, 400, 500, 100))
                    boardgame.board_arr=np.zeros(shape=(3,3))
                    text = font.render(PlayerTurn.name, 1, (255, 255, 255))
                    text_rect = text.get_rect(center =(width / 2, 500-50))
                    screen.blit(text, text_rect)
                    print("Play again")
                    pg.display.update()
                    clock.tick(fps)
                    continue

    if(PlayerTurn==Player.AI):
        tempBoard=np.copy(boardgame.board_arr)
        s,i,j=AI.minimax(tempBoard,Player.AI)

        time.sleep(0.5)
        posx=(j)*width/3+30
        posy=(i)*width/3+30
        screen.blit(x_img, (posx, posy))
        status=boardgame.addMove(i,j,PlayerTurn.value)
        if status!=Player.Playing:
                screen.fill ((0, 0, 0), (0, 400, 500, 100))
                text = font.render(status.name, 1, (255, 255, 255))
                text_rect = text.get_rect(center =(width / 2, 500-50))
                screen.blit(text, text_rect)
                PlayerTurn=status
        else:
                PlayerTurn=Player.Person
                screen.fill ((0, 0, 0), (0, 400, 500, 100))
                text = font.render(PlayerTurn.name, 1, (255, 255, 255))
                text_rect = text.get_rect(center =(width / 2, 500-50))
                screen.blit(text, text_rect)
        continue
    
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and PlayerTurn==Player.Person:
            x,y=pg.mouse.get_pos()
            
            i,j=Input.User_Click(x,y,width,height)
            if(boardgame.board_arr[i][j]==-2 or boardgame.board_arr[i][j]==2):
                continue
            posx=(j)*width/3+30
            posy=(i)*width/3+30
            screen.blit(o_img, (posx, posy))
            
            status=boardgame.addMove(i,j,PlayerTurn.value)
            if status!=Player.Playing:
                screen.fill ((0, 0, 0), (0, 400, 500, 100))
                text = font.render(status.name, 1, (255, 255, 255))
                text_rect = text.get_rect(center =(width / 2, 500-50))
                screen.blit(text, text_rect)
                PlayerTurn=status
            else:
                if(PlayerTurn==Player.AI):
                    PlayerTurn=Player.Person
                else:
                    PlayerTurn=Player.AI
                screen.fill ((0, 0, 0), (0, 400, 500, 100))
                text = font.render(PlayerTurn.name, 1, (255, 255, 255))
                text_rect = text.get_rect(center =(width / 2, 500-50))
                screen.blit(text, text_rect)
      
    pg.display.update()
    clock.tick(fps)