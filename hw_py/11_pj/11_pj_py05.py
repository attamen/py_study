import re
example1='저는 91년에 태어남.97년에 imf가 있었다. 지금은 2023년이다.'
a=re.findall(r'\d.+년',example1)
print(a)