from random import randint
import tkinter as tk
from functools import partial
from itertools import product

fieldsX, fieldsY = 9, 9 ## determine gameboard x and y
buttonW, buttonH = 3,1 ## setting size of buttons
lst = [[0 for _ in range(fieldsX)] for _ in range(fieldsY)] ##creates dynamically 2d list
#lst = ([""]*fieldsX,[""]*fieldsX,[""]*fieldsX) ## filling with n copies 

positions = product(range(fieldsY), range(fieldsX))
#mines = randint(1,9)

mines = 10
buttonIdentities = []
#buttonIdentities = {} ##when naming buttons needs to be {}

def change(i):
	bname=(buttonIdentities[i])
	buttonPosition = ([int(i/fieldsX),i%fieldsX]) #gets list position
	buttPosX = int(i/fieldsX)
	buttPosY = i%fieldsX
	print(buttPosY,buttPosX)
	bname.configure(text=lst[buttPosX][buttPosY], relief=tk.SUNKEN)
	if lst[buttPosX][buttPosY] == "*":
		print("BOOM you're dead")
		"""for a in range(0,fieldsX*fieldsY):
			bname=(buttonIdentities[a])
			bname.configure(text=lst[buttPosX][buttPosY], relief=tk.SUNKEN)"""
	else:
		minesCount = 0
		if lst[buttPosX-1][buttPosY] == "*":
			minesCount =+ 1
		elif lst[buttPosX+1][buttPosY] == "*":
			minesCount =+ 1
		elif lst[buttPosX-1][buttPosY-1] == "*":
			minesCount =+ 1
		elif lst[buttPosX][buttPosY-1] == "*":
			minesCount =+ 1
		elif lst[buttPosX+1][buttPosY-1] == "*":
			minesCount =+ 1		
		elif lst[buttPosX-1][buttPosY+1] == "*":
			minesCount =+ 1
		elif lst[buttPosX][buttPosY+1] == "*":
			minesCount =+ 1
		elif lst[buttPosX+1][buttPosY+1] == "*":
			minesCount =+ 1
		print (minesCount)
		bname.configure(text=minesCount, relief=tk.SUNKEN)
for i in range (0,mines):
	randomX=randint(0,fieldsX-1)
	randomY=randint(0,fieldsY-1)
	lst[randomY][randomX] = "*"

root = tk.Tk()
root.title("Minesweeper")
root.minsize(width=fieldsX*buttonW, height=fieldsY*buttonH)

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