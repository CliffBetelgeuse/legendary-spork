from turtle import*
from random import*
from time import*

'''
自己编的生命游戏，也能够自己独立编写完成了，尽管实现过一遍
自己再做一次还是会遇到各种坑，这次遇到的是缩进坑，太烦人了
实在是太烦人了pytho
'''
class Cell(Turtle):

	def __init__(self,x,y):
		Turtle.__init__(self,shape='square')
		self.ht()
		self.speed(0)
		self.shapesize(1)
		self.color('yellow','gray')
		self.up()
		self.goto(x,y)
		self.st()
		self.now=False
		self.next=False
		self.neighbors=[]
	def act(self):

		if self.now==True:
			self.color('yellow','red')
		else:
			self.color('yellow','gray')
		count=0
		for n in self.neighbors:
			if n.now==True:
				count+=1
		if count>=3 and count<=5:
			self.next=True
		else:
			self.next=False

	def upd(self):
		self.now=self.next

class World:
	def __init__(self,n):
		cells=[]
		for i in range(n):
			row=[]
			for j in range(n):
				c=Cell(-n*10+j*20,n*10-i*20)
				row.append(c)
			cells.append(row)
		self.cells=cells
		self.n=n
	def get_neighbors(self):     #这个地方真是坑死了，千万不要tab和空格混用，千万不要，缩进烦死人
		for i in range(self.n):
			for j in range(self.n): 
				if j>0:
					self.cells[i][j].neighbors.append(self.cells[i][j-1])
				if j<self.n-1:
					self.cells[i][j].neighbors.append(self.cells[i][j+1])
				if i>0 :
					self.cells[i][j].neighbors.append(self.cells[i-1][j])
				if i<self.n-1:
					self.cells[i][j].neighbors.append(self.cells[i+1][j])
				if i>0 and j>0:
					self.cells[i][j].neighbors.append(self.cells[i-1][j-1])
				if i>0 and j<self.n-1:
					self.cells[i][j].neighbors.append(self.cells[i-1][j+1])
				if i<self.n-1 and j<self.n-1:
					self.cells[i][j].neighbors.append(self.cells[i+1][j+1])
				if i<self.n-1 and j>0:
					self.cells[i][j].neighbors.append(self.cells[i+1][j-1])
				print(i,j)

	def life_start(self):
		for i in range(self.n):
			for j in range(self.n):
				self.cells[i][j].act()
		for i in range(self.n):
			for j in range(self.n):
				self.cells[i][j].upd()

tracer(1600,1)

w=World(40)
w.get_neighbors()
'''
for i in range(10):
	for j in range(10):
		print(len(w.cells[i][j].neighbors))
'''

for i in range(200):
	x=randint(0,39)
	y=randint(0,39)
	w.cells[x][y].now=True

while 1:
	w.life_start()
	sleep(0.5)








