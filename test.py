table = []
push  = table.append

for i in range(0,8):
    for j in range(i+1,9):
        for k in range(j+1,10):
            push('' + str(i) + str(j) + str(k))


print(table)
           