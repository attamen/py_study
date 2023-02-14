a=""

for i in range(1,6):
    if i<=3:
        j=i
    else:
        j=6-i

    for k in range(3,j,-1):
        a+=" "
    for l in range(0,2*j-1):
        a+="*"
    a+='\n'

print(a)
            
