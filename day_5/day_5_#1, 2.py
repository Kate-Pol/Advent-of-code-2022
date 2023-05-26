with open("day_5.txt") as file:
    lines = file.read()
    stacks_string, instructions = (i.splitlines() for i in lines.strip('\n').split('\n\n'))


stacks = {int(digit):[] for digit in stacks_string[-1].replace(" ", "")}

indexes = [index for index, char in enumerate(stacks_string[-1]) if char != " "]

# used to display the contants in each stack
def display_stacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

def load_stacks():
    for string in stacks_string[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

def empty_stacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ''
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

load_stacks() 

# ---- part 1 ------

for instruction in instructions:    
    instruction = instruction.replace('move ', '').replace('from ', '').replace('to ', '').strip().split(' ')
    instruction = [int(i) for i in instruction] 
    
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    
    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

               
print('Part 1: ', getStackEnds())


# ---- part 2 -----

empty_stacks()
load_stacks()

for instruction in instructions:    
    instruction = instruction.replace('move ', '').replace('from ', '').replace('to ', '').strip().split(' ')
    instruction = [int(i) for i in instruction] 
    
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    
    crates_to_remove = stacks[from_stack][-crates:]     # finding out whoch crate to remove 
    stacks[from_stack] = stacks[from_stack][:-crates]   # removing crates 
    
    for crate in crates_to_remove:
        stacks[to_stack].append(crate)    # adding crates to oa different stack
        
    
print('part 2: ', getStackEnds())
        