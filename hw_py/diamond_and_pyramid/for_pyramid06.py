a=""

for i in range(0,5):
    for j in range(0,i):
        a+=" "

    for k in range(5,i,-1):
        a+="*"

    a+='\n'

print(a)