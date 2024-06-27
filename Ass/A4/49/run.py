import colorama
from colorama import Fore, Back, Style
from getch import KBHit
from time import time,sleep
import numpy as np 
import globals

from alarmexception import AlarmException
from board import board
from mando import *
from os import system
from random import randint
import signal

#from mando import empty

def pos(x, y):
    return '\x1b[%d;%dH' % (y, x)
quick=2    
gamestart=time()    
xcor=3
ycor=42
system('tput civis')
start=time()
stl1=time()
stl2=time()
stl3=time()
player=Mandalorian(xcor,ycor,quick)
kb=KBHit()
score=0
lives=9
sheild=0
shtime=0
comp= -60          
enemy=0
dragonlife=5
exist=0
Mflag=0
scenary=Hills(0,0,quick)
scenary2=Hills2(100,0,quick)
Mtime=time()+1000
t=0
dogflag=0
coins = [ 0 for i in range(1000)]
ccount=0
coins[ccount]=Coin(199,randint(17,40),quick)
laser1 = [ 0 for i in range(1000)]
l1count=0
laser2 = [ 0 for i in range(1000)]
l2count=0
laser3 = [ 0 for i in range(1000)]
l3count=0
dragontype=0
bullet = [ 0 for i in range(1000)]
bcount=0

lightsaber = [ 0 for i in range(1000)]
sabercount=0

void = [ 0 for i in range(1000)]
vcount=0

while 1:

    dragontype=dragontype+1

    #acceleration in gravity
    if player.rety()==42:
        t=0
    if exist==1:
        player.gravity(sheild,0,dragontype)    
    else:
        t=player.gravity(sheild,t,dragontype)
    try:
        if time()-speedstart > 5:
            quick=2
    except:
        pass        
    try:
        if villain.rety()<36:        
            villain.gravity(t)
    except:
        pass
    
    board.makegrid()
    inp=kb.getinput()


   # time duration for shield
    if time()-shtime > 10 and sheild == 1:
        sheild=0
        comp=time()
    
    #initializing coins
    if time() - start > 2 and time() - gamestart < 60:
        #print("blah")
        start= time()
        ccount=ccount+1
        coins[ccount]=Coin(199,randint(17,40),quick)

    #speedup
    if time() - gamestart > 4 and Object.sflag==0:
        
        flash=Speed(199,randint(18,40),quick)
        Object.sflag=1
    try:   
        flash.moveleft()      
    except:
        pass

    #magnet
    if time() - gamestart > 20 and Mflag==0:
        magnet=Magnet(randint(30,180),15,quick)
        Mflag=1
        exist=1
        Mtime=time()

    if exist==1:
        if magnet.retx()>player.retx():
            player.moveright(sheild,dragontype)
        elif magnet.retx()<player.retx():
            player.moveleft(sheild,dragontype)    
        player.moveup(sheild,dragontype)

    if time()-Mtime > 4:
        exist=0
        try:
            Void(magnet.retx()-1,magnet.rety(),quick)
            del(magnet)
        except:
            pass

    #Snowballs of villain            
    if time() - gamestart > 61 and time() - saber > 2:
        lightsaber[sabercount]=Lightsaber(170,player.rety()+3,quick)
        sabercount = sabercount +1
        saber=time()

    try:
        if board.arr[flash.retx()-1][flash.rety()]!=" " and board.arr[flash.retx()-1][flash.rety()]!="|" and board.arr[flash.retx()-1][flash.rety()]!="-" and board.arr[flash.retx()-1][flash.rety()]!="\\":
            speedstart=time()
            quick=3
            del flash
    except:
        pass                   

    #bullets of mando
    for i in range(len(bullet)):
        try :
            if bullet[i].retx() > -2 :
                bullet[i].moveright()   
                if board.arr[bullet[i].retx()+5][bullet[i].rety()]!=" " and board.arr[bullet[i].retx()+5][bullet[i].rety()]!="|" and board.arr[bullet[i].retx()+5][bullet[i].rety()]!="-" and board.arr[bullet[i].retx()+5][bullet[i].rety()]!="\\" and board.arr[bullet[i].retx()+5][bullet[i].rety()]!="o" and board.arr[bullet[i].retx()+5][bullet[i].rety()]!="B":
                    dragonlife=dragonlife-1
                    del bullet[i] 

        except:
            pass

    #checking collisions of coins
    for i in range(len(coins)):
        try :
            if coins[i].retx() > -2 :
                coins[i].moveleft(globals.coins)
                
                if board.arr[coins[i].retx()-1][coins[i].rety()]!=" " and board.arr[coins[i].retx()-1][coins[i].rety()]!="|" and board.arr[coins[i].retx()-1][coins[i].rety()]!="-" and board.arr[coins[i].retx()-1][coins[i].rety()]!="\\"and board.arr[coins[i].retx()-1][coins[i].rety()]!="B":
                    score = score +10
                    del coins[i]
                if board.arr[coins[i].retx()][coins[i].rety()-1]!=" " and board.arr[coins[i].retx()][coins[i].rety()-1]!="|" and board.arr[coins[i].retx()][coins[i].rety()-1]!="-" and board.arr[coins[i].retx()][coins[i].rety()-1]!="\\"and board.arr[coins[i].retx()][coins[i].rety()-1]!="B":
                    score = score + 10
                    del coins[i]
                if board.arr[coins[i].retx()-1][coins[i].rety()-1]!=" " and board.arr[coins[i].retx()-1][coins[i].rety()-1]!="|" and board.arr[coins[i].retx()-1][coins[i].rety()-1]!="-" and board.arr[coins[i].retx()-1][coins[i].rety()-1]!="\\"and board.arr[coins[i].retx()-1][coins[i].rety()-1]!="B":
                   score = score + 10
                   del coins[i]     
                if board.arr[coins[i].retx()][coins[i].rety()+1]!=" " and board.arr[coins[i].retx()][coins[i].rety()+1]!="|" and board.arr[coins[i].retx()][coins[i].rety()+1]!="-" and board.arr[coins[i].retx()][coins[i].rety()+1]!="\\"and board.arr[coins[i].retx()][coins[i].rety()+1]!="B":
                    score = score + 10   
                    del coins[i]
                if board.arr[coins[i].retx()-1][coins[i].rety()+1]!=" " and board.arr[coins[i].retx()-1][coins[i].rety()+1]!="|" and board.arr[coins[i].retx()-1][coins[i].rety()+1]!="-" and board.arr[coins[i].retx()-1][coins[i].rety()+1]!="\\"and board.arr[coins[i].retx()-1][coins[i].rety()+1]!="B":
                    score = score + 10   
                    del coins[i]    
        except:
            pass


    if time() - stl1 > 5 and time() - gamestart < 60:
        stl1= time()
        
        laser1[l1count]=Laser1(199,randint(19,40),quick)
        l1count=l1count+1

    #checking collisions of laser1
    for i in range(len(laser1)):
        try :
            if laser1[i].retx() > -2 :
                laser1[i].moveleft(globals.laser1)
                delx=laser1[i].retx()
                dely=laser1[i].rety()
                if board.arr[laser1[i].retx()-1][laser1[i].rety()]!=" " and board.arr[laser1[i].retx()-1][laser1[i].rety()]!="|" and board.arr[laser1[i].retx()-1][laser1[i].rety()]!="-" and board.arr[laser1[i].retx()-1][laser1[i].rety()]!="\\" and board.arr[laser1[i].retx()-1][laser1[i].rety()]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()]!="B":
                        #print("1")
                        lives = lives -1
                    del laser1[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1
                if board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!=" " and board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="|" and board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="-" and board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="\\"and board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="B":
                        lives = lives -1
                        #print("2")
                    del laser1[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1
                if board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!=" " and board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="|" and board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="-" and board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="\\"and board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="B":
                        lives = lives -1
                        #print("3")
                    del laser1[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1    
            else:
                del(laser1[i])
                       
        except:
            pass
    
    if time() - stl2 > 3 and time() - gamestart < 60:
        stl2= time()
        
        laser2[l2count]=Laser2(190,randint(19,40),quick)
        l2count=l2count+1

    #checking collisions of laser2
    for i in range(len(laser2)):
        try :
            if laser2[i].retx() > -2 :
                laser2[i].moveleft(globals.laser2)
                delx=laser2[i].retx()
                dely=laser2[i].rety()
                if board.arr[laser2[i].retx()-1][laser2[i].rety()]!=" " and board.arr[laser2[i].retx()-1][laser2[i].rety()]!="|" and board.arr[laser2[i].retx()-1][laser2[i].rety()]!="-" and board.arr[laser2[i].retx()-1][laser2[i].rety()]!="\\"and board.arr[laser2[i].retx()-1][laser2[i].rety()]!="S"  and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()]!="B":
                        lives = lives -1
                        #print("4")
                    del laser2[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1
                if board.arr[laser2[i].retx()-1][laser2[i].rety()-1]!=" " and board.arr[laser2[i].retx()-1][laser2[i].rety()-1]!="|" and board.arr[laser2[i].retx()-1][laser2[i].rety()-1]!="-" and board.arr[laser2[i].retx()-1][laser2[i].rety()-1]!="\\"and board.arr[laser2[i].retx()-1][laser2[i].rety()-1]!="S"  and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()-1]!="B":
                        lives = lives -1
                        #print("5")
                    del laser2[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1
                if board.arr[laser2[i].retx()-1][laser2[i].rety()+1]!=" " and board.arr[laser2[i].retx()-1][laser2[i].rety()+1]!="|" and board.arr[laser2[i].retx()-1][laser2[i].rety()+1]!="-" and board.arr[laser2[i].retx()-1][laser2[i].rety()+1]!="\\"and board.arr[laser2[i].retx()-1][laser2[i].rety()+1]!="S"  and sheild==0:
                    if board.arr[laser1[i].retx()-1][laser1[i].rety()+1]!="B":
                        lives = lives -1
                        #print("6")
                    del laser2[i]
                    void[vcount]=Void(delx-3,dely,quick)
                    vcount=vcount+1        
            else:
                del laser2[i]       

        except:
            pass

    if time() - stl3 > 4 and time() - gamestart < 60:
        stl3= time()
        
        laser3[l3count]=Laser3(190,randint(19,40),quick)
        l3count=l3count+1
    
    #checking collisions of laser3
    for i in range(len(laser3)):
        try :
            if laser3[i].retx() > -2 :
                laser3[i].moveleft(globals.laser3)
                delx=laser3[i].retx()
                dely=laser3[i].rety()
                if board.arr[laser3[i].retx()-1][laser3[i].rety()]!=" " and board.arr[laser3[i].retx()-1][laser3[i].rety()]!="|" and board.arr[laser3[i].retx()-1][laser3[i].rety()]!="-" and board.arr[laser3[i].retx()-1][laser3[i].rety()]!="\\"and board.arr[laser3[i].retx()-1][laser3[i].rety()]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-3][laser1[i].rety()]!="B":
                        lives = lives -1
                        #print("7")
                    del laser3[i]
                    void[vcount]=Void(delx-1,dely,quick)
                    vcount=vcount+1
                if board.arr[laser3[i].retx()-1][laser3[i].rety()-1]!=" " and board.arr[laser3[i].retx()-1][laser3[i].rety()-1]!="|" and board.arr[laser3[i].retx()-1][laser3[i].rety()-1]!="-" and board.arr[laser3[i].retx()-1][laser3[i].rety()-1]!="\\"and board.arr[laser3[i].retx()-1][laser3[i].rety()-1]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-3][laser1[i].rety()-1]!="B":
                        lives = lives -1
                        #print("8")
                    del laser3[i]
                    void[vcount]=Void(delx-1,dely,quick)
                    vcount=vcount+1
                if board.arr[laser3[i].retx()-1][laser3[i].rety()+1]!=" " and board.arr[laser3[i].retx()-1][laser3[i].rety()+1]!="|" and board.arr[laser3[i].retx()-1][laser3[i].rety()+1]!="-" and board.arr[laser3[i].retx()-1][laser3[i].rety()+1]!="\\"and board.arr[laser3[i].retx()-1][laser3[i].rety()+1]!="S" and sheild==0:
                    if board.arr[laser1[i].retx()-3][laser1[i].rety()+1]!="B":
                        lives = lives -1
                        #print("9")
                    del laser3[i]
                    void[vcount]=Void(delx-1,dely,quick)
                    vcount=vcount+1
            else:
                del laser3[i]        
        except:
            pass


    #checking collisions of snowballs
    for i in range(len(lightsaber)):
        try :
            if lightsaber[i].retx() > -2 :
                lightsaber[i].moveleft(globals.lightsaber)
                
                if board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!=" " and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!="|" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!="-" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!="\\"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!="B"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()]!="S" and sheild==0:
                    lives = lives - 1
                    del lightsaber[i]
                if board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!=" " and board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!="|" and board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!="-" and board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!="\\"and board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!="B"and board.arr[lightsaber[i].retx()][lightsaber[i].rety()-1]!="S" and sheild==0:
                    lives = lives - 1
                    del lightsaber[i]
                if board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!=" " and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!="|" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!="-" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!="\\"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!="B"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()-1]!="S" and sheild==0:
                   lives = lives - 1
                   del lightsaber[i]     
                if board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!=" " and board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!="|" and board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!="-" and board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!="\\"and board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!="B"and board.arr[lightsaber[i].retx()][lightsaber[i].rety()+1]!="S" and sheild==0:
                    lives = lives - 1   
                    del lightsaber[i]
                if board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1]!=" " and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1]!="|" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1]!="-" and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1]!="\\"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1]!="B"and board.arr[lightsaber[i].retx()-1][lightsaber[i].rety()+1   ]!="S" and sheild==0:
                    lives = lives - 1   
                    del lightsaber[i]    
        except:
            pass

    #initializing enemy
    if time() - gamestart > 60 and enemy==0:
        villain=Enemy(170,player.rety()-6,quick)
        Void(player.retx()+8,player.rety(),quick)
        sheild=0
        enemy=1
        saber=time()

    #movements of mando
    if inp == "w":
        t=0
        player.moveup(sheild,dragontype)
        try:
            villain.moveup()
        except:
            pass    
    elif inp == "a":
        player.moveleft(sheild,dragontype)
    elif inp == "d":
        player.moveright(sheild,dragontype)
    elif inp == "b":
        bcount=bcount+1
        bullet[bcount]=Bullet(player.retx()+12,player.rety(),quick)
    elif inp == ' ' and time() - comp > 60:
        shtime=time()
        sheild=1
    elif inp == "j" and dogflag==0 and score > 50:
        dogflag=1
        sheild=2
    elif inp == "q":
        system('tput cnorm')
        quit()

    #all the print statements of screen    
    print('%s%s%s%s' % (pos(2, 50),Back.RESET,Fore.RESET, score))
    if enemy==0:
        print('%s%s%s%s%s' % (pos(2, 51),Back.RESET,Fore.RESET, "Time Left=",int(60-(time()-gamestart))))
    else:
        print('%s%s%s%s' % (pos(2, 51),Back.RESET,Fore.RESET,"BOSS FIGHT!!!!"))    
    print('%s%s%s%s%s' % (pos(2, 52),Back.RESET,Fore.RESET,"Total Life =", str(lives)))

    #Victory condition
    if dragonlife<=0:
        score = score + 50   
        Victory(100,17,quick)
        board.makegrid()
        break

    #defeat condition
    if lives < 0:
        Defeat(100,17,quick)
        board.makegrid()
        break
        
print(Back.RESET,Fore.RESET,"Total Score=",score)