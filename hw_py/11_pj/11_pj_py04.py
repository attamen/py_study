import re
number='my number is 511223-1****** and yours is 521012-2******'
a=re.findall('\d{6}',number)
print(a)