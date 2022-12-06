def data_arrangement(data):
    global instructions, df, lines, df, crate_stacks_0
    lines = data.read().splitlines()
    spacer = lines.index('')
    crate_stacks = lines[:spacer-1]
    no_cols=int(lines[spacer-1].split()[-1])
    crate_stacks_0=[]
    for i in range(0,no_cols):
        stacks=[]
        for j in range(0,len(crate_stacks)):
            stacks.append(crate_stacks[j][(i*4)+1])
        crate_stacks_0.append(stacks)
    instructions = lines[spacer+1:]
    
def parse_instructions(instructions):
    global instructions_list
    instructions_list=[]
    for i in range (0,len(instructions)):
        list_string = instructions[i].split()
        int_list = [x for x in list_string if x.isalpha()==False]
        instructions_list.append(int_list)

def highest_crate(crate_stacks_0,col):
    for i in range(0,len(crate_stacks_0[col])):
        if crate_stacks_0[col][i] != " ":
            return i
    return len(crate_stacks_0[col])-1

def next_empty(crate_stacks_0,col):
        for i in range(len(crate_stacks_0[col])-1,-1,-1):
            if crate_stacks_0[col][i] == " ":
                return i
               
def pick_crate(crate_stacks_0,col,amount_to_move,move_to):
    global crates_to_move
    highest_crate_ind=highest_crate(crate_stacks_0,col)
    if highest_crate_ind ==len(crate_stacks_0[col])-1:
        print('crate is at end')
    crates_to_move=crate_stacks_0[col][highest_crate_ind:highest_crate_ind +amount_to_move]
    
    for i in range(0,len(crates_to_move)):
        crate_stacks_0[col][highest_crate_ind+i]=" "
    for i in range(len(crates_to_move)-1,-1,-1):
        moving_location=next_empty(crate_stacks_0,move_to)
        if moving_location == None:
            crate_stacks_0[move_to].insert(0,crates_to_move[i])
        else:
            crate_stacks_0[move_to][moving_location]=crates_to_move[i]
        
def move_crate(crate_stacks_0,crate_to_move,move_from,move_to,crate_to_move_ind):
    if next_empty(crate_stacks_0,move_to) == None:
        crate_stacks_0[move_to].insert(0,crate_to_move)
    else:
        crate_stacks_0[move_to][next_empty(crate_stacks_0,move_to)]=crate_to_move
    crate_stacks_0[move_from][crate_to_move_ind]=" "

    
data=open('input.txt','r')
data_arrangement(data)
parse_instructions(instructions)

for i in range(0,len(instructions_list)):
    
    amount_to_move=int(instructions_list[i][0])
    move_from=int(instructions_list[i][1])-1
    move_to=int(instructions_list[i][2])-1
    
    if amount_to_move==1:
        crate_to_move_ind = highest_crate(crate_stacks_0,move_from)
        crate_to_move=crate_stacks_0[move_from][crate_to_move_ind]
        move_crate(crate_stacks_0,crate_to_move,move_from,move_to,crate_to_move_ind)
        print(crate_stacks_0)
    else:
        pick_crate(crate_stacks_0,move_from,amount_to_move,move_to)
        print(crate_stacks_0)
            
for i in range(0,len(crate_stacks_0)):
    crate_to_move_ind = highest_crate(crate_stacks_0,i)
    crate_to_move=crate_stacks_0[i][crate_to_move_ind]
    print(crate_to_move)


