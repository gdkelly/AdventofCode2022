alfa='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfa_priority={}
for i in range(0,len(alfa)):
    alfa_priority[alfa[i]]=i+1
    
data=open('input.txt','r')
rucksacks=[x for x in data.read().splitlines()]
priority_sum=0
for i in range(0,len(rucksacks)):
    no_items=int(len(rucksacks[i]))
    no_items_half =int(no_items/2)
    comp_1=[x for x in rucksacks[i][0:(no_items_half)]]
    comp_2=[x for x in rucksacks[i][no_items_half:no_items]]
    union = set(comp_1) & set(comp_2)
    matches = [x for x in union]
    for j in range(0,len(matches)):
        priority_sum+=alfa_priority[matches[j]]
print(priority_sum)

priority_sum=0
i=0
while i < len(rucksacks):
    union = set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]) 
    matches = [x for x in union]
    for j in range(0,len(matches)):
        priority_sum+=alfa_priority[matches[j]]
    i+=3
print(priority_sum)