a=int(input("몇 명?>"))
students=[]
#입력
for i in range(a):
    name=input("이름>")
    sub_1=int(input("점수-1>"))
    sub_2=int(input("점수-2>"))
    sub_3=int(input("점수-3>"))
#리스트화       
    student=[name,sub_1,sub_2,sub_3]
    students.append(student)

#항목출력
print("이름","총점","평균","학점",sep='\t')
#연산
for j in students:
    sum=j[1]+j[2]+j[3]
    w=(sum/3)
    if 90<=w<=100:
        score="A"
    elif 80<=w<90:
        score="B"    
    elif 70<=w<80:
        score="C"   
    else:
        score="F"
    if w%10>5 and w>70 or w==100:
        score+="+"
#내용출력
    print(j[0],sum,"{:.2f}".format(w),score,sep='\t') 



      



