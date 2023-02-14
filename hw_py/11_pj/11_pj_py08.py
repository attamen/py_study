import re
example='이동민 교수는 다음과 같이 설명(이동민,2019).그런데 다른 교수는 이 문제에 대해 이렇게(최재영,2019).또 다른 견해도 있었다(lion,2018)'
result=re.findall(r'\(.+?\)',example)
print(result)