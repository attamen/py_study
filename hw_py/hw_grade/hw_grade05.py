a=int(input("몇 명?>"))
students=[]
#입력
for i in range(a):
    name=input("이름>")
    sub_1=int(input("점수-1>"))
    sub_2=int(input("점수-2>"))
    sub_3=int(input("점수-3>"))

#연산
def info(student):
    student=[name,sub_1,sub_2,sub_3]
    s.append(student)

class Student:
    def __init__(self,name,s_1,s_2,s_3):
        self.name=name
        self.s_1=s_1
        self.s_2=s_2
        self.s_3=s_3

    def sum(self):
        return self.s_1+self.s_2+self.s_3
    def aver(self):
        return self.sum(self)
    def string(self):
        return "{}\t{}\t{}".format(self.name,self.sum(),self.aver())


for j in students:
    w=sum()/3
    if 90<=w<=100:
        score="A"
    elif 80<=w<90:
        score="B"    
    elif 70<=w<80:
        score="C"   
    else:
        score="F"
    if w%10>=5 and w>70 or w==100:
        score+="+"
#항목출력
    print("이름","총점","평균","학점",sep='\t')
#내용출력
    print(j[0],sum,"{:.2f}".format(w),score,sep='\t') 
