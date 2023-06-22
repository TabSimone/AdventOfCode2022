import re

#FIRST PART
file_path = "AdventOfCode2022/06/input.txt"
#Array to use to add packets of 4 letters to check if they are different
array = []
#Variable to memorize the position the correct packet
i=3
# Open the .txt file
with open(file_path, "r") as file:
    file_content = file.read()
    for char in file_content: #I parse character by character in the array
        array.append(char) 
        if(len(array) == 4): 
            i += 1
            #check if an array have all different elements
            if(len(array) == len(set(array))): 
                #WHen you pass an array to set, it removes exery duplciate. Sets are made this way
                break    
            else:
                array.pop(0)
            
print(i)

#SECOND PART
#A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
#I just need to change array to 14
array_second = []
i=13
# Open the .txt file
with open(file_path, "r") as file:
    file_content = file.read()
    for char in file_content: 
        array_second.append(char) 
        if(len(array_second) == 14): 
            i += 1
            if(len(array_second) == len(set(array_second))): 
                break    
            else:
                array_second.pop(0)
print(i)


