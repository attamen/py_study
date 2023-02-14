import datetime

now=datetime.datetime.now()

a=input("12시간제 or 24시간제?(입력 시 숫자로 12 혹은 24)")
a=float(a)

if a==12:
    if now.hour==0 or now.hour==24:
        print("현재 시각은 오전 12시입니다.")
    elif 0<now.hour<12:
        print("현재 시각은 오전 {}시입니다.".format(now.hour))
    elif now.hour==12:
        print("현재 시각은 오후 12시입니다.")
    else:
        print("현재 시각은 오후 {}시입니다.".format(now.hour-12))

elif a==24:
    if 0<now.hour<12:
        print("현재 시각은 오전 {}시입니다.".format(now.hour))
    else:
        print("현재 시각은 오후 {}시입니다.".format(now.hour))

else:
    print("입력이 잘못되었습니다. 다시 입력해주세요.")