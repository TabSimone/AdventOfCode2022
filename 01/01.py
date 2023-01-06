maxSum = 0
currentSum = 0

with open(r".\01\input.txt") as file:
    for line in file:
        if(line == '\n') :
            if(maxSum < currentSum):
                maxSum = currentSum
            currentSum = 0        
        else :
            currentSum = currentSum + int(line)
        
print(maxSum)