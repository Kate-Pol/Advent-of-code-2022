with open('day_2_#1.txt') as f:
 
    d = [i for i in f.read().strip().split('\n')]
    
print(d)
        
# possible outcomes:

# A Y = 2 + 6 = 8 won
# A X = 1 + 3 = 4 draw
# A Z = 3 + 0 = 3 lost
# B Y = 2 + 3 = 5 draw
# B X = 1 + 0 = 1 lost
# B Z = 3 + 6 = 9 won
# C Y = 2 + 0 = 2 lost
# C X = 1 + 6 = 7 won
# C Z = 3 + 3 = 6 draw

outcome = {
    'A Y':8, 'A X':4, 'A Z':3,
    'B Y':5, 'B X':1, 'B Z':9,
    'C Y':2, 'C X':7, 'C Z':6
}

total = 0
for j in d:
    total += outcome[j]

print(total)
