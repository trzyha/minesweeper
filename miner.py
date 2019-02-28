from random import randint
import tkinter as tk
from functools import partial
from itertools import product

fieldsX, fieldsY = 5, 5 ## determine gameboard x and y
buttonW, buttonH = 3,1 ## setting size of buttons
lst = (["",]*fieldsX,)*fieldsY
positions = product(range(fieldsX), range(fieldsY))
#mines = randint(1,9)

mines = 5
#buttonIdentities = []
buttonIdentities = {}

def change(i):
	bname=(buttonIdentities[i])
	#bname.configure(text=i, relief=tk.SUNKEN)


#print(len(lst))
for y in range (0, len(lst)):
	for x in range (0,3):
		mineYesNo = randint(1,2)
		if mineYesNo == 1:
			lst[y][x] = "*"

print(lst)


root = tk.Tk()
root.title("Minesweeper")
root.minsize(width=fieldsX*buttonW, height=fieldsY*buttonH)
"""for iY in range(fieldsY):
	for iX in range(fieldsX):
		btn = tk.Button(root, width=2, command=partial(change,iX,iY))
		btn.grid(row=iY, column=iX)
		buttonIdentities.append(btn)"""
"""for i, item in enumerate(positions):
    button = tk.Button(root, command=partial(change, i),width=buttonW, height=buttonH)
    button.grid(row=item[0], column=item[1], sticky="n,e,s,w")
    buttonIdentities.append(button)"""

for iX in range(fieldsX):
    for iY in range(fieldsY):
        buttonIdentities[(iX,iY)]=tk.Button(root,text='%s/%s'%(iX,iY),borderwidth=10)
        buttonIdentities[iX,iY].grid(row=iX,column=iY)


print(buttonIdentities)
if __name__ == '__main__':
	root.mainloop()