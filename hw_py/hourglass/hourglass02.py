while True:
    i_t=input("몇 줄의 모래시계를 원하십니까>")
    it=int(i_t)
    if it%2==0 and 4<=it<=20:
        a=""
        for i in range(-(it//2-1),it//2,1):
            for j in range((it//2-1)-abs(i)):
                a+=' '
            for k in range(1+2*abs(i)):
                a+="*"
            a+='\n'

        print(a)

    elif it==0:
        print("종료합니다")
        break
    else:
        print("4 이상 20 이하의 짝수만 가능합니다 다시 입력해주세요")