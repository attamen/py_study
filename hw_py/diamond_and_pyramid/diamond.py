while True:
    input_text=input("몇 줄의 다이아몬드를 원하세요?")
    i_t=int(input_text)
    if i_t%2==1 and 3<=i_t<=19:
        a=' '
        for i in range(-((i_t-1)/2), ((i_t-1)/2)+1,1):
            for j in range(abs(i)):
                a+=' '
            for k in range(i_t-2*abs(i)):
                a+='*'

            a+='\n'
        print(a)

    elif i_t==0:
        print("종료합니다")
        break

    else:
        print("3 이상 20 이하의 홀수만 입력합니다")

    