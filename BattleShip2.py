import random
list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b=random.randint(0,7)
shipCol = (list1[b])
shipRow = random.randint(1, 8)
#print (shipCol)
#print (shipRow)
guessRow = int (input ("Please guess the row (1-8): "))
guessCol = str (input("Please guess the column (a-h): "))
if shipCol == guessCol and shipRow == guessRow:
    print ("Hit")
else:
    print ("Miss")