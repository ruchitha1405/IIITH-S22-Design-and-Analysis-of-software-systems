
from board import board
from globals import *
from scenary import *
from colorama import Fore, Back, Style
class Object:
    def __init__(self,x,y,velx):
        self._x = x
        self._y = y
        self._velx=velx
    sflag=0    
    def rety(self):
        return self._y

    def retx(self):
        return self._x

    def setvel(self,a):
        self._vel=self._vel+a    

    def add(self,a,flag = "empty"):
        for i in range(len(a)):
            for j in range(len(a[i])):
                board.arr[self._x+j][self._y+i] = ' ' if flag is "empty" else a[i][j]
    
    def moveleft(self,i):
        if self._x > 3:
            self.add(i,)
            self._x = self._x -self._velx
            self.add(i,"aa") 

class Mandalorian(Object):
    
    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(mando,"aa")

    def gravity(self,shield,i,typ):
        if shield==0:
            if self._y < 42:
                self.add(mando,)
                self._y = self._y + i
                if self._y>42:
                    self._y=42 
                self.add(mando,"aa")
        elif shield==1:
            if self._y < 42:
                self.add(safe,)
                self._y = self._y +i
                if self._y>42:
                    self._y=42 
                self.add(safe,"aa")  
        elif shield==2:
            if typ%3==0:
                if self._y < 42:
                    self.add(drogon1,)
                    self._y = self._y +i
                    if self._y>42:
                        self._y=42 
                    self.add(drogon1,"aa")
            elif typ%3==1:
                if self._y < 42:
                    self.add(drogon2,)
                    self._y = self._y +i
                    if self._y>42:
                        self._y=42 
                    self.add(drogon2,"aa")
            elif typ%3==2:
                if self._y < 42:
                    self.add(drogon3,)
                    self._y = self._y +i
                    if self._y>42:
                        self._y=42 
                    self.add(drogon3,"aa")        
        i=i+1
        return i
    def moveup(self,shield,typ):
        if shield==0:
            if self._y>19:
                self.add(mando,)
                self._y = self._y-5        
                self.add(mando,"aa")
        elif shield==1:
            if self._y>19:
                self.add(safe,)
                self._y = self._y-5        
                self.add(safe,"aa") 

        elif shield==2:
            if typ%3==0:
                if self._y>19:
                    self.add(drogon1,)
                    self._y = self._y-5        
                    self.add(drogon1,"aa")              
            elif typ%3==1:
                if self._y>19:
                    self.add(drogon2,)
                    self._y = self._y-5        
                    self.add(drogon2,"aa")
            elif typ%3==2:
                if self._y>19:
                    self.add(drogon3,)
                    self._y = self._y-5        
                    self.add(drogon3,"aa")        
    def moveleft(self,shield,typ):
        if shield==0:
            if self._x > 3:
                self.add(mando,)
                self._x = self._x -2 
                self.add(mando,"aa") 
        elif shield==1:
            if self._x > 3:
                self.add(safe,)
                self._x = self._x -2 
                self.add(safe,"aa")
                
        elif shield==2:
            if typ%3==0:
                if self._x > 3:
                    self.add(drogon1,)
                    self._x = self._x -2 
                    self.add(drogon1,"aa")
            elif typ%3==1:
                if self._x > 3:
                    self.add(drogon2,)
                    self._x = self._x -2 
                    self.add(drogon2,"aa")
            elif typ%3==2:
                if self._x > 3:
                    self.add(drogon3,)
                    self._x = self._x -2 
                    self.add(drogon3,"aa")            

    def moveright(self,shield,typ):
        if shield==0:
            if self._x<60:
                self.add(mando,)
                self._x = self._x +2 
                self.add(mando,"aa")
        elif shield==1:
            if self._x<60:
                self.add(safe,)
                self._x = self._x +2 
                self.add(safe,"aa")      

        elif shield==2:
            if typ%3==0:
                if self._x<60:
                    self.add(drogon1,)
                    self._x = self._x +2 
                    self.add(drogon1,"aa")
            elif typ%3==1:        
                if self._x<60:
                    self.add(drogon2,)
                    self._x = self._x +2 
                    self.add(drogon2,"aa")
            elif typ%3==2:
                if self._x<60:
                    self.add(drogon3,)
                    self._x = self._x +2 
                    self.add(drogon3,"aa")            
class Coin(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(coins,"aa")
    

               

class Magnet(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(magnet,"aa")

class Lightsaber(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(lightsaber,"aa")
    

                 

class Speed(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(speed,"aa")

    def moveleft(self):
        if self._x > 3:
            self.add(speed,)
            self._x = self._x -self._velx
            self.add(speed,"aa") 
class Bullet(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(bullet,"aa")

    def moveright(self):
        if self._x < 199:
            self.add(bullet,)
            self._x = self._x +self._velx
            self.add(bullet,"aa")                  

class Laser1(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(laser1,"aa")


     

class Laser2(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(laser2,"aa")
   



class Laser3(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(laser3,"aa")


class Hills(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(hills,"aa")            

class Hills2(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(hills2,"aa")         
class Victory(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(victory,"aa")

class Defeat(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(defeat,"aa")

class Enemy(Object):
    
    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(enemy,"aa")

    def gravity(self,i):
        if self._y < 36:
            self.add(enemy,)
            self._y = self._y +i
            if self._y>36:
                self._y=36 
            self.add(enemy,"aa")

    def moveup(self):
        if self._y>19:
            self.add(enemy,)
            self._y = self._y-5        
            self.add(enemy,"aa")

    def moveleft(self):
        if self._x > 3:
            self.add(enemy,)
            self._x = self._x -2 
            self.add(enemy,"aa")   

    def moveright(self):
        if self._x<60:
            self.add(enemy,)
            self._x = self._x +2 
            self.add(enemy,"aa")        

class Void(Object):

    def __init__(self,x,y,velx):
        super().__init__(x,y,velx)
        self.add(void,"aa")
