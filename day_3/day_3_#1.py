with open('day_3.txt') as f:
 
    words = [i for i in f.read().strip().split('\n')]   
print(words)

total = 0

for word in words:
    let_list = []
    i1 = word[:len(word)//2]
    i2 = word[len(word)//2:]
    print(i1, i2)
    
    def same_character(i1, i2):
        global total
        for char in i1:
            if char in i2:
                if char.islower():
                    total += (ord(char)-96)
                elif char.isupper():
                    total += (ord(char)-38)
                #return char, ord(char)
                return total
    print(same_character(i1, i2))





