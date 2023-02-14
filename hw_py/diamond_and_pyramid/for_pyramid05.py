a=""

for i in range(1,5):
    for j in range(4,i,-1):
        a+=' '
    for k in range(0,2*i-1):
        a+="*"

    a+='\n'

print(a)