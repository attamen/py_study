a=''

for i in range(0,4):
    for k in range(0,i):
        a+=" "
    
    for j in range(2*(4-i)-1,0,-1):
        a+="*"

    

    a+='\n'

print(a)
print(reversed(a))