list=[]
for i in range(9):
 list.append(int(input()))
length=len(list)
length=int(length/3)
chunk1=[]
stat=0
stop=3

for i in range(length):
    chunk1=list[stat:stop]
    print(chunk1)
    chunk1.reverse()
    print(chunk1)
    stat=stop
    stop=stop+3