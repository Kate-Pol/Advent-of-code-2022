with open('day_1_#1.txt') as f:
    lines = f.readlines()
    
    max_1 = 0
    max_2 = 0
    max_3 = 0
    total = 0

    for x in lines:
        if x != '\n':
            total += int(x)
        elif x == '\n':
            total = 0
        

        if total > max_1:
            max_1 = total
        elif total > max_2:
            max_2 = total
        elif total > max_3:
            max_3 = total

            
            
            
    print(max_1 + max_2 + max_3)
