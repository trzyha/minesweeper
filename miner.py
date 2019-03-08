from random import randint
import tkinter as tk
from functools import partial
from itertools import product

def createBoard(fieldsX,fieldsY,mines):
	fieldsX, fieldsY = 9, 9 ## determine gameboard x and y
	buttonW, buttonH = 3,1 ## setting size of buttons
	lst = [[0 for _ in range(fieldsX)] for _ in range(fieldsY)] ##creates dynamically 2d list
#lst = ([""]*fieldsX,[""]*fieldsX,[""]*fieldsX) ## filling with n copies 
	mines = 10
	positions = product(range(fieldsY), range(fieldsX))
#mines = randint(1,9)

fieldsX, fieldsY = 10, 10 ## determine gameboard x and y
buttonW, buttonH = 3,1 ## setting size of buttons
lst = [[0 for _ in range(fieldsX)] for _ in range(fieldsY)] ##creates dynamically 2d list
#lst = ([""]*fieldsX,[""]*fieldsX,[""]*fieldsX) ## filling with n copies 
mines = 10
positions = product(range(fieldsY), range(fieldsX))

buttonIdentities = []
#buttonIdentities = {} ##when naming buttons needs to be {}
createBoard(10,10,10)
def change(i):
	buttPosX = int(i/fieldsX)
	buttPosY = i%fieldsX
	if lst[buttPosX][buttPosY] == "*":
		print("BOOM you're dead")
		buttonIdentities[i].configure(text="*", relief=tk.SUNKEN, bg="#f47142")
#	elif lst[buttPosX][buttPosY] = 0

	else:
		bname=(buttonIdentities[i])
		buttonPosition = ([int(i/fieldsX),i%fieldsX]) #gets list position

		print(buttPosY,buttPosX)
		bname.configure(text=lst[buttPosX][buttPosY], relief=tk.SUNKEN)
		checkAround(buttPosX, buttPosY, i, "*")

def checkAround(buttPosX, buttPosY, i, fieldChar):
	minesCount = 0
	try:
		if lst[buttPosX-1][buttPosY] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX+1][buttPosY] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX-1][buttPosY-1] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX][buttPosY-1] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX+1][buttPosY-1] == fieldChar:
			minesCount = minesCount + 1	
		if lst[buttPosX-1][buttPosY+1] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX][buttPosY+1] == fieldChar:
			minesCount = minesCount + 1
		if lst[buttPosX+1][buttPosY+1] == fieldChar:
			minesCount = minesCount + 1
	except:
		pass

	bname=(buttonIdentities[i])
	print (minesCount)
	bname.configure(text=minesCount, relief=tk.SUNKEN)

for i in range (0,mines):
	randomX=randint(0,fieldsX-1)
	randomY=randint(0,fieldsY-1)
	lst[randomY][randomX] = "*"

root = tk.Tk()
root.title("Minesweeper")
root.minsize(width=fieldsX*buttonW, height=fieldsY*buttonH)

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label = "Game", menu=filemenu)
filemenu.add_command(label="Small board (10x10 - 10 mines")
filemenu.add_command(label="Medium board (20x20 - 30 mines")
filemenu.add_command(label="Big board (35x35 - 120 mines")
filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit)


for i, item in enumerate(positions):
    button = tk.Button(root, command=partial(change, i),width=buttonW, height=buttonH)
    button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
    buttonIdentities.append(button)

"""for iX in range(fieldsX):  ##naming buttons worth to remember
    for iY in range(fieldsY):
        buttonIdentities[(iX,iY)]=tk.Button(root,text='%s/%s'%(iX,iY),borderwidth=10)
        buttonIdentities[iX,iY].grid(row=iX,column=iY)"""


if __name__ == '__main__':
	root.mainloop()