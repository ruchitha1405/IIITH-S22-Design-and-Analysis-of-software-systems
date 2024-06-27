import numpy as np 
import colorama
from colorama import Fore, Back, Style
import time

def pos(x, y):
    return '\x1b[%d;%dH' % (y, x)

sizex=200
sizey=48

display=200
class board:
    a=[[" "]*sizey]*sizex
    arr=np.array(a,dtype=str)
    arr[:, sizey-1]="T"
    #arr[8][sizey-1]="P"

    def makegrid():
       for i in range(len(board.arr)-4):
           ycount=0
           for j in range(len(board.arr[i])):
                if i>5:
                    if j<15:
                        print('%s%s%s%s' % (pos(i, j),Back.GREEN,Fore.BLACK, board.arr[i][j]))
                    elif j <47:
                        print('%s%s%s%s' % (pos(i, j),Back.CYAN,Fore.RED, board.arr[i][j])) 
                    else:
                        print('%s%s%s%s' % (pos(i, j),Back.CYAN,Fore.BLUE, board.arr[i][j]))
                elif i==5:
                    print('%s%s' % (pos(i, j), " "))
                    