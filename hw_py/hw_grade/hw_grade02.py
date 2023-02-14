a=int(input("몇 명?"))

for i in range(1,a+1):
    s=input("이름?")
    p=int(input("점수-1:"))
    q=int(input("점수-2:"))
    r=int(input("점수-3:"))
    w=(p+q+r)/3

    print("<",s,">")
    print("총점:",p+q+r)
    print("평균:",(p+q+r)/3)

    if 95<=w<=100:
        print("학점:A+")
    elif 90<=w<95:
        print("학점:A")    
    elif 85<=w<90:
        print("학점:B+")
    elif 80<=w<85:
        print("학점:B")
    elif 75<=w<80:
        print("학점:C+")
    elif 70<=w<75:
        print("학점:C")    
    else:
        print("학점:F")