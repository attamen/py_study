a=""

for i in range(0,3):
    for j in range(2,i,-1):
        a+=" "
    for k in range(0,2*i+1):
        a+="*"
    a+='\n'

for l in range(0,2):
    for m in range(0,l+1):
        a+=" "
    for n in range(-2*l+3,0,-1):
        a+="*"

    a+='\n'
print(a)
                                            