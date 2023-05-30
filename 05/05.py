import re

table = []

with open(r"C:\Users\SEDD\Documents\GitHub\AdventOfCode2022\05\input2.txt") as file:
    for line in file:
        if(line[0] != "m" and len(line)>1):    
            arr = []
            counter = 0
            counterCharacter = 0
            for x in line:
                if(counter == 1):
                    arr.append(line[1])
                if(counter == 5):
                    arr.append(line[counterCharacter])
                    counter = 1
                counter+=1  
                counterCharacter+=1
            counterCharacter = 0
            table.append(arr)
        else:
            arrWithMoves = re.findall(r'\d+', line)
            if(len(arrWithMoves) > 1):
                print("")
print(table)
