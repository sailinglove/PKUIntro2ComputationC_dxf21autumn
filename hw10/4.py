import re

lst = re.findall('\d+', input())

for i in lst:
    temp = i.lstrip('0')
    if temp:
        print(temp)