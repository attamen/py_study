while True:
    input_text=input("몇 줄?")
    it=int(input_text)

    if it%2==0 and 4<=it<=20:
        for i in range(1,it//2+1):
            print('*'*(it-2*i-1)+' '*i)
        for j in range(it//2):
            print('*'*(2*j+1)+' '*j)

    elif it==0:
        print("종료")
        break
    else:
        print("4 이상 20 이하의 짝수만 가능 다시 입력하세요")