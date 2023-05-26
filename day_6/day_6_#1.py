with open('day_6.txt') as f:
    words = f.read().strip() 

for i in range(4, len(words)):
    s = set(words[(i-4):i])
    if len(s) == 4:
        print(i)
        break