a=[1,2,4,5,6,3,5,3,4,5,3]
c={}

for i in a:
    if i not in c:
        c[i]=0
    c[i]+=1

print("a에서 사용된 숫자의 종류는 {}개".format(len(c)))