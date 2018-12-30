# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 11:57:55 2018

@author: DELL
"""

board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
select=['','']
def printboard():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("   |   |   ")
    print("------------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("   |   |   ")
    print("------------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("   |   |   ")

def selectmarker():
    while select[0]!='X' and select[0]!='O':
        select[0]=input("Player 1 : Pease pick a marker X OR 0 : ").upper()
        if(select[0]=='X'):
            select[1]='O'
        else:
            select[1]='X'
            
def mark_in_board(num,mark):
    if(num==1):
            board[2][0]=mark
    elif num==2:
        board[2][1]=mark
    elif num==3:
        board[2][2]=mark
    elif num==4:
        board[1][0]=mark
    elif num==5:
        board[1][1]=mark
    elif num==6:
        board[1][2]=mark
    elif num==7:
        board[0][0]=mark
    elif num==8:
        board[0][1]=mark
    elif num==9:
        board[0][2]=mark

def win_check(mark):
    for i in range(3):
        if board[i][0]==mark and board[i][1]==mark and board[i][2]==mark:
            return True
        if board[0][i]==mark and board[1][i]==mark and board[2][i]==mark:
            return True
    if board[0][0]==mark and board[1][1]==mark and board[2][2]==mark:
        return True
    if board[0][2]==mark and board[1][1]==mark and board[2][0]==mark:
        return True
    
    
      
while input("do you want to play yes/No :").lower()=="yes":
    board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    select=['','']        
    printboard()
    for i in range(1,10):
        selectmarker()
        if(i%2!=0):
            pos=int(input("player 1 : enter the position (1-9) :"))
            mark_in_board(pos,select[0])
            if win_check(select[0]):
                print("PLAYER 1 WIN THE MATCH ")
                printboard()
                break
        else:
            pos=int(input("player 2 : enter the position (1-9) :"))
            mark_in_board(pos,select[1])
            if win_check(select[1]):
                print("PLAYER 2 WIN THE MATCH ")
                printboard()
                break
        printboard()
    