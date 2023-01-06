firstPartResult = 0
secondPartResult = 0
counter = 0

with open(r".\03\input2.txt") as file:

    rucksack1 = ""
    rucksack2 = ""
    rucksack3 = ""
    value = 0
    for line in file:
        print(line.splitlines())
        arrayOfLine = list(line)

        #First Part
        firstRucksacks = arrayOfLine[:int((len(arrayOfLine)/2))]
        secondRucksacks = arrayOfLine[int((len(arrayOfLine)/2)):]
        
        #Clean line break
        if "\n" in secondRucksacks:
                secondRucksacks.remove("\n")

        #Use intersection to find common Element + from array to single character
        commonElement = ''.join(set(firstRucksacks).intersection(secondRucksacks))

        #Now I can calculate the value, based on ASCII
        if(commonElement.islower()):
                firstPartResult = firstPartResult + ord(commonElement)-96
        else:
                firstPartResult = firstPartResult + ord(commonElement)-38

        #Second Part
        if(counter == 0):
                rucksack1 = arrayOfLine
                counter += 1
        elif(counter==1):
                rucksack2 = arrayOfLine
                counter += 1
        elif(counter==2):
                rucksack3 = arrayOfLine
                counter = 0
                value = set(rucksack1) & set(rucksack2) & set(rucksack3)
                print(value)
#print(firstPartResult)
