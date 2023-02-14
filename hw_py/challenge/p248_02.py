limit=10000
i=1
sum_value=0
while sum_value<=limit:
    if i==1:
        i+i+1==sum_value
        i=i+1
    else:
        i=i+1
        sum_value=sum_value+i

print("{}을 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))