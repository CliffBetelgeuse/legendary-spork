from tkinter import*
from time import*
from random import *


class Star:
    def __init__(self,x,y,z,canvas):
        self.x=x
        self.y=y
        self.z=z
        self.canvas=canvas
        colors=["red",'yellow','blue','green','white']
        color=choice(colors)
        self.id=canvas.create_oval(x-10+z/20,y-10+z/20,x+10-z/20,y+10-z/20,fill=color)
        self.px=x
        self.py=y
        self.trace=canvas.create_line(x,y,x,y,fill=color)
        self.c_h=self.canvas.winfo_height()
        self.c_w=self.canvas.winfo_width()

    def move(self):
        dx=0
        dy=0
        if self.z<=10:
            self.z=200

            self.x=randint(200,1400)
            self.y=randint(200,800)                
        else:
            dx=(self.x-0.5*self.c_w)/(self.z)*4
            dy=(self.y-0.5*self.c_h)/(self.z)*4
            self.x+=dx
            self.y+=dy
            self.z-=2
            canvas.move(self.id,dx,dy)
            
        x=self.x
        y=self.y
        z=self.z
        #canvas.coords(self.id,x,y,x,y)
        #canvas.coords(self.trace,self.x-3*dx,self.y-3*dy,self.x,self.y)
        canvas.coords(self.id,x-10+z/20,y-10+z/20,x+10-z/20,y+10-z/20)
        

tk=Tk()

canvas=Canvas(tk,width=1000,height=1000,background='black')
canvas.pack()
tk.update()     #这一句一定要加，否则window未设置，宽高还会是1，self.c_h=self.canvas.winfo_height()


stars=[]
for i in range(0,300):
    stars.append(Star(randint(200,800),randint(200,800),randint(0,200),canvas))


while 1:
    for star in stars:
        star.move()
    tk.update()


        
        
    
