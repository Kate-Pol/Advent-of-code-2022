with open('day_1_#1.txt') as f:
    lines = f.readlines()
    
    max_number = 0
    total = 0
    
    for x in lines:
        if x != '\n':
            total += int(x)
        elif x == '\n':
            total = 0
        
        if total > max_number:
            max_number = total
            
    print(max_number)
