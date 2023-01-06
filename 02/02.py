resultsOne = [ 
        "A X" , 1 + 3,
        "A Y" , 2 + 6,
        "A Z" , 3 + 0,
        "B X" , 1 + 0,
        "B Y" , 2 + 3,
        "B Z" , 3 + 6,
        "C X" , 1 + 6,
        "C Y" , 2 + 0,
        "C Z" , 3 + 3,
]

resultsTwo = [ 
        "A X" , 3 + 0,
        "A Y" , 1 + 3,
        "A Z" , 2 + 6,
        "B X" , 1 + 0,
        "B Y" , 2 + 3,
        "B Z" , 3 + 6,
        "C X" , 2 + 0,
        "C Y" , 3 + 3,
        "C Z" , 1 + 6,
]

sumOne = 0
sumTwo = 0

with open(r".\02\input.txt") as file:
    for line in file:
        sumOne = sumOne + resultsOne[resultsOne.index(line.rstrip('\n')) + 1]
        sumTwo = sumTwo + resultsTwo[resultsTwo.index(line.rstrip('\n')) + 1]


print(sumOne)
print(sumTwo)
