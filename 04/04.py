import re

sumOfFull = 0
sumOfPartial = 0

with open(r".\04\input.txt") as file:
    for line in file:
        
        arrayOfLine = re.split(',|-', line.rstrip('\n'))

        #First Part
        #Two condition: the first one if first group major than second, the second one the opposite
        if(int(arrayOfLine[0]) <= int(arrayOfLine[2]) and int(arrayOfLine[1]) >= int(arrayOfLine[3]) or int(arrayOfLine[2]) <= int(arrayOfLine[0]) and int(arrayOfLine[3]) >= int(arrayOfLine[1])):
                sumOfFull += 1

        
        if(int(arrayOfLine[1]) >= int(arrayOfLine[2]) and int(arrayOfLine[0]) <= int(arrayOfLine[3])  ):
                sumOfPartial += 1
                
print(sumOfFull)
print(sumOfPartial)