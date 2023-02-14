a=int(input("몇 명?>"))
dictionary=[]
#노트참고(for문 두 개 별개로, 이중x)
for i in range(1,a+1):
    n=input(str(i)+"-"+"이름?>")
    output=0
    for j in range(1,4):
        s=int(input("점수-{}는?>".format(j)))
        output+=s
        w=output/3
        #A+만 제거       
        if w==100:
            score="A+"
        elif 90<=w<100:
            score="A"
        elif 80<=w<90:
            score="B"    
        elif 70<=w<80:
            score="C"   
        else:
            score="F"

        #형전환 대신 %5 이용
        #100도 예외로 하지 않고 연산할 수 있게
        w=str(w)

        last_number=w[-1]

        if last_number in '56789':
            score += "+"
        
        w=float(w)

        dic={
        "name":n,
        "total":output,
        "average":w,
        "score":score
        }

        
    dictionary.append(dic)

print(dictionary)

#평균 소수점 두 자리로 포현하기
#이름 총점 평균 학점

        