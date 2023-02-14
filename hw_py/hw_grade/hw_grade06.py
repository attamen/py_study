i=0
a=int(input("몇 명?>"))
sum=0
avg=0
while i<a:
    scores=int(input("점수>"))
    sum+=scores
    list.append(scores)
    i+=1

avg=sum/a
