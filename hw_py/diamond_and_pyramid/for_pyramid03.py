a=""

for i in range(1,6):
    for j in range(5,0,-1):
        a+=(" "*j)
        for k in range(1,i):
            a+=("*"*k)
            a+="\n"

print(a)

