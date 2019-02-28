from random import randint
import tkinter as tk
from functools import partial
from itertools import product

fieldsX, fieldsY = 6, 3 ## determine gameboard x and y
buttonW, buttonH = 3,1 ## setting size of buttons
lst = (["",]*fieldsX,)*fieldsY
positions = product(range(fieldsY), range(fieldsX))
#mines = randint(1,9)
i=0
mines = 5
buttonIdentities = []
#buttonIdentities = {} ##when naming buttons needs to be {}

def change(i):
	bname=(buttonIdentities[i])
	buttonPosition = ([int(i/fieldsX),i%fieldsX]) #gets list position
	buttPosX = int(i/fieldsX)
	buttPosY = i%fieldsX
	#print(buttPosX, buttPosY) ##testing position
	#print(lst[buttPosX][buttPosY])
	bname.configure(text=lst[buttPosX][buttPosY], relief=tk.SUNKEN)
	if lst[buttPosX][buttPosY] == "*":
		print("BOOM you're dead")



for i in range (1,mines+1)
	randomX=randint(0,fieldsX-1)
	randomY=randint(0,fieldsY-1)
	#if lst[randomX-1][randomY-1] != "*":
	lst[1][1] = "*"
	print(randomX, randomY)
	#lst[randomX-1][randomY-1] = "*"

#print(len(lst))
"""for y in range (0, fieldsY):
	for x in range (0,fieldsX):
		mineYesNo = randint(1,3)
		if mineYesNo == 1:
			lst[y][x] = "*"""
			
print(lst)


root = tk.Tk()
root.title("Minesweeper")
root.minsize(width=fieldsX*buttonW, height=fieldsY*buttonH)
"""for iY in range(fieldsY):
	for iX in range(fieldsX):
		btn = tk.Button(root, width=2, command=partial(change,iX,iY))
		btn.grid(row=iY, column=iX)
		buttonIdentities.append(btn)"""

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