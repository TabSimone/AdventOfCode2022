import re

matrix = [["C", "Z", "N", "B", "M", "W", "Q", "V"],
    ["H", "Z", "R", "W", "C", "B"],
    ["F", "Q", "R", "J"],
    ["Z", "S", "W", "H", "F", "N", "M", "T"],
    ["G", "F", "W", "L", "N", "Q", "P"],
    ["W", "L", "P"],
    ["V", "B", "D", "R", "G", "C", "Q", "J"],
    ["Z", "Q", "N", "B", "W"],
    ["H", "L", "F", "C", "G", "T", "J"]]

#FIRST PART

with open(r".\05\input.txt") as file:
    """
    print("FIRST PART")
    for line in file:
        #I get position 1,3,5 from array splitting, where 1 is quantity, 3 is start, 5 is finish
        array = line.split(" ")
        i = int(array[1])
        while i > 0:
            #I add last element in the matrix 
            matrix[int(array[5])-1].append(matrix[int(array[3])-1][-1])
            #I remove last element in the matrix
            matrix[int(array[3])-1].pop()
            i = i -1
    y = 0
    while y < len(matrix):
        (matrix[y][-1])
        y += 1 
    """
    print("SECOND PART")
    for line in file:
        #I get position 1,3,5 from array splitting, where 1 is quantity, 3 is start, 5 is finish
        array = line.split(" ")
        i = int(array[1])
        while i > 0:
            #I add last element in the matrix using quantity to get the index
            matrix[int(array[5])-1].append(matrix[int(array[3])-1][-i])    
            i = i -1
        #After I finished copying, I remove last elements in the row where I started
        row = matrix[int(array[3])-1]
        matrix[int(array[3])-1] = row[:-int(array[1])] 

    y = 0
    while y < len(matrix):
        print(matrix[y][-1])
        y += 1 

