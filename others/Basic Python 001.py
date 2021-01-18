f = open('math', 'r')
i = f.readline()

sum = int(i)

while i:
    i = f.readline()
    print(i[0], i[2:-2], len(i))
    
    if(i[0] == '+'):
        sum += int(i[2:-2])
    else:
        sum -= int(i[2:-2])
    print(sum)

print(hex(sum))


#f.close()
