from random import randint

lst = (["","",""],["","",""],["","",""],["","",""])
#mines = randint(1,9)

mines = 5


print (mines)
#print(len(lst))
for y in range (0, len(lst)):
	for x in range (0,3):
		mineYesNo = randint(1,2)
		if mineYesNo == 1:
			lst[y][x] = "*"

print(lst)
