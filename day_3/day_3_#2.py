from string import ascii_letters

with open('day_3.txt') as f:
    words = [i for i in f.read().strip().split('\n')]   

total = 0
for word in words:
    half = len(word)//2
    
    left = word[:half]
    right = word[half:]
    
    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            total += priority + 1
print("part 1: ", total)




j = 3
total = 0
for i in range(0, len(words), 3):
    rucksacks = words[i:j]
    j += 3
    
    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            total += priority + 1
            
print("part 2: ", total)
        



