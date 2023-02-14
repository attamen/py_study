student=[]
students=[]
i=0
sum=0
a=int(input("몇 명?"))
for k in range(a):
    name=input("이름?")
    student.append(name)
    while i<3:
        score=int(input("점수>"))
        sum+=score
        i+=1
    student.append(sum)
    w=sum/3
    student.append(sum/3)
    i=0
    
    if 90<=w<=100:
        grade="A"
    elif 80<=w<90:
        grade="B"    
    elif 70<=w<80:
        grade="C"   
    else:
        grade="F"
    if (w%10>=5 and w>70) or w==100:
        grade+="+"
    student.append(grade)
    students.append(student)
#항목출력
print("이름","총점","평균","학점",sep='\t')
#내용출력
for student in students:
    print(name,sum,"{:.2f}".format(w),grade,sep='\t')

