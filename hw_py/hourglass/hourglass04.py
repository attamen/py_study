while True:
    input_text=input("몇 줄?")
    it=int(input_text)

    if it%2==0 and 4<=it<=20:
        for i in range(it//2):
            print(' '*i+'*'*(-2*i+it-1))
        for j in range(it//2):
            print(' '*(it//2-1,-1,-1)+'*'*(2*j+1))

    elif it==0:
        print("종료")
        break
    else:
        print("4 이상 20 이하의 짝수만 가능 다시 입력하세요")