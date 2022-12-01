data = open('input.txt','r')
calories_list=[x for x in data.read().splitlines()]
elf=0
elves=[]

for i in range(0,len(calories_list)):
    if calories_list[i] != '':
        elf+=int(calories_list[i])
    if calories_list[i]=='' or i==len(calories_list)-1:
        elves.append(elf)
        elf=0

elves=sorted(elves)
number_to_sum = 3
calories=0
for i in range(1,number_to_sum+1):
    calories+=elves[-i]
print(calories)
