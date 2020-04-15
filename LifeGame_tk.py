#！python3

from tkinter import*
from time import*
from random import *
import itertools

L=50

class Cell:
    def __init__(self,x,y,canvas):
        self.canvas=canvas
        self.id=canvas.create_rectangle(x-5,y-5,x+5,y+5,fill='green')
        
        self.neighbour=[]
        self.now=False
        self.next=False
        self.rep_max_num=3
        self.rep_mini_num=3
        self.survive_max_num=3
        self.survive_mini_num=2
    def set_live(self):
        self.now=True
        canvas.itemconfig(self.id,fill='red')
    def set_dead(self):
        self.now=False
        canvas.itemconfig(self.id,fill='green')
    def set_laws(self,a,b,c,d):
        self.rep_max_num=a     #之前这里系成了 rep_num_max 这就是名字起得复杂惹的祸，找了半天的bug，我说怎么繁殖法则没有改变啊！
        self.rep_mini_num=b
        self.survive_max_num=c
        self.survive_mini_num=d
    def act(self):
        if self.now==True:
            canvas.itemconfig(self.id,fill='red')
        else:
            canvas.itemconfig(self.id,fill='green')
        count=0
        for n in self.neighbour:
            if n.now:
                count+=1
        if self.now==True and count>=self.survive_mini_num and count<=self.survive_max_num:
            self.next=True
        elif self.now==False and count>=self.rep_mini_num and count<=self.rep_max_num:
    
            self.next=True 
        else:
            self.next=False
    def update(self):
        self.now=self.next
        self.next=False

window=Tk()
window.title("生命游戏")
canvas=Canvas(window,width=L*10,height=L*10+150,background='orange')
canvas.pack()

cells=[]  #世界初始化，L×L的方格世界将每个cell和自己的邻居连接好
        
for i in range(L):
    row=[]
    for j in range(L):
        cell=Cell(5+i*10,5+j*10,canvas)
        row.append(cell)
    cells.append(row)

for i in range(0,L):
    for j in range(0,L):
        if i>0:
            cells[i][j].neighbour.append(cells[i-1][j])
            if j>0:
                cells[i][j].neighbour.append(cells[i-1][j-1])
            if j<L-1:
                cells[i][j].neighbour.append(cells[i-1][j+1])               
        if i<L-1:
            cells[i][j].neighbour.append(cells[i+1][j])
            if j>0:
                cells[i][j].neighbour.append(cells[i+1][j-1])
            if j<L-1:
                cells[i][j].neighbour.append(cells[i+1][j+1])
        if j>0:
            cells[i][j].neighbour.append(cells[i][j-1])
        if j<L-1:
            cells[i][j].neighbour.append(cells[i][j+1])


def initiate(event):    #响应鼠标点击，改变当前状态
    x,y=event.x,event.y
    if y<=L*10:
        column=x//10
        row=y//10
        cell=cells[column][row]
        if cell.now==True:
            cell.set_dead()
        else:
            cell.set_live()
        

canvas.bind("<Button-1>", initiate)

go=True
def start():
    global go
    go=True
    while go:
        for row in cells:
            for cell in row:
                cell.act()
        for row in cells:
            for cell in row:
                cell.update()
        #sleep(0.01)
        window.update()

def pause():
    global go
    go=False
        
def clear():
    global go
    go=False
    for row in cells:
            for cell in row:
                cell.set_dead()
def set_nums(a,b,c,d):
    #print(a,b,c,d)
    for row in cells:
            for cell in row:
                cell.set_laws(int(a),int(b),int(c),int(d))
                
def random_initiate(n):
   
    xs=range(0,L)
    ys=range(0,L)
    samples=itertools.product(xs,ys)
    coords=sample(list(samples),int(n))
    for c in coords:
        x=c[0]
        y=c[1]
        cells[x][y].set_live()
    




b1 = Button(window, text='开启', bg='blue', width=5,font=('Arial',12),command=lambda:start())   #设计按钮
b1.place(x='20', y='520')
b2 = Button(window, text='暂停', bg='yellow', width=5,font=('Arial',12),command=lambda:pause())   #设计按钮
b2.place(x='20', y='560')
b3 = Button(window, text='清除', bg='red',width=5, font=('Arial',12),command=lambda:clear())   #设计按钮
b3.place(x='20', y='600')




e1=Entry(window,width=5)
e1.place(x='100',y='520')

e2=Entry(window,width=5)
e2.place(x='150',y='520')

l1 = Label(window, text='存活条件范围\n 最大、最小值', bg='orange', font=('Arial',10))   #设置说明
l1.place(x='100', y='550')

         
e3=Entry(window,width=5)
e3.place(x='220',y='520')

e4=Entry(window,width=5)
e4.place(x='270',y='520')

l2 = Label(window, text='繁殖条件范围\n最大、最小值',bg='orange', font=('Arial',10))   #设计标题
l2.place(x='220', y='550')

b4 = Button(window, text='重设生存法则', bg='pink',width=10, font=('Arial',10),command=lambda:set_nums(e3.get(),e4.get(),e1.get(),e2.get()))   #设计按钮
b4.place(x='170', y='600')


e5=Entry(window,width=8)  #e5=e3=Entry(window,width=8)居然犯了这种错误
e5.place(x='330',y='520')

b5 = Button(window, text='随机生存\n数开始', bg='cyan',width=7, font=('Arial',10),command=lambda:random_initiate(e5.get()))   #设计按钮
b5.place(x='330', y='550')

window.update()     #这一句一定要加，否则window未设置，宽高还会是1，self.c_h=self.canvas.winfo_height()






'''
            

'''



