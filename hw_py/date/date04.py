time=input("현재 시각은?")
t=int(time)

if 1<=t<=12:
    a=input("오전 혹은 오후?")
    if a=="오전":
        print("오전입니다")
    elif a=="오후":
        print("오후입니다")
    else:
        print("다시 입력해주세요")    
elif t==0 or t==24:
    print("현재는 오전입니다")

elif 13<=t<=23:
    print("현재는 오후입니다")

else:
    print("다시 입력해주세요")


    