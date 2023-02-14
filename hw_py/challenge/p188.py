a=input("입력:")
import datetime


if "안녕" in a:
    print("그래요 반가워요")

elif "몇 시" in a:
    now=datetime.datetime.now()
    print(f"지금은 {now.hour}시")

else:
    print(a)