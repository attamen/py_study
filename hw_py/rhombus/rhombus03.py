a=""

for i in range(-2,3):
    for j in range(abs(i)):
        a+=" "
    for k in range(-2*abs(i)+5):
        a+="*"

    a+='\n'

print(a)