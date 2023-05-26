with open('day_6.txt') as f:
    words = f.read().strip() 

for i in range(14, len(words)):
    s = set(words[(i-14):i])
    if len(s) == 14:
        print(i)
        break