#Using ASCII to return value
def elementToValue(element):
 if(element.islower()):
        return ord(element)-96
 else:
        return ord(element)-38

with open(r".\03\input.txt") as file:
    firstPartResult = 0 
    secondPartResult = 0   
    counter = 0
    for line in file:
        arrayOfLine = list(line.rstrip('\n'))

        #First Part
        firstRucksacks = arrayOfLine[:int((len(arrayOfLine))/2)]
        secondRucksacks = arrayOfLine[int((len(arrayOfLine))/2):]

        #Use intersection to find common Element + from array to single character
        commonElement = ''.join(set(firstRucksacks).intersection(secondRucksacks))
        firstPartResult += elementToValue(commonElement)

        #Second Part
        if(counter == 0):
                rucksack1 = arrayOfLine
                counter += 1
        elif(counter==1):
                rucksack2 = arrayOfLine
                counter += 1
        elif(counter==2):
                counter = 0
                secondPartResult += elementToValue(''.join(set(rucksack1) & set(rucksack2) & set(arrayOfLine)))

print(firstPartResult)
print(secondPartResult)

