import re

f = open(r'C:\Users\Administrator\Desktop\redata.txt')
for eachLine in f:
    patt = '\w+\s(\w+)\s(\d+)\s[\d:]+\s(\d+)'
    MDY = re.findall(patt, eachLine)
    print(MDY)
