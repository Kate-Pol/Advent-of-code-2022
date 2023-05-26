with open('day_2_#1.txt') as f:
 
    d = [i for i in f.read().strip().split('\n')]
    
print(d)
        
# possible outcomes:
# 1 for Rock (A) 
# 2 for Paper (B) 
# 3 for Scissors (C)

# 0 - lost (X), 3 - draw (Y), and 6 - won (Z)

# A Y = 1 + 3 = 4 draw
# A X = 3 + 0 = 3 lost
# A Z = 2 + 6 = 8 won
# B Y = 2 + 3 = 5 draw
# B X = 1 + 0 = 1 lost
# B Z = 3 + 6 = 9 won
# C Y = 3 + 3 = 6 draw
# C X = 2 + 0 = 2 lost
# C Z = 1 + 6 = 7 won

outcome = {
    'A Y':4, 'A X':3, 'A Z':8,
    'B Y':5, 'B X':1, 'B Z':9,
    'C Y':6, 'C X':2, 'C Z':7
}

total = 0
for j in d:
    total += outcome[j]

print(total)
