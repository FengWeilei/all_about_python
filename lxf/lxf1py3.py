##https://github.com/michaelliao/learn-python3/blob/master/samples/functional/do_reduce.py

from functools import reduce
def str2float(s):
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
    def fn1(x,y):
        return x * 10 + y
    def fn2(x,y):
        return x / 10 + y
    
    SL = s.split('.')
    def char2num(s):
        return DIGITS[s]
    SL2 = ''
    for i in range(len(SL[1])):
        SL2 += SL[1][-1-i]
	
    result1 = reduce(fn1, map(char2num, SL[0]))
    result2 = reduce(fn2, map(char2num, SL2))/10
    result = result1 + result2
    return result

print(str2float('123.456'))


##>>> 'a'.lower()
##'a'
##>>> 'a'.upper()
##'A'
##>>> def normalize(name):
##    Name = name[0].upper()
##    for i in name[1:]:
##        Name += i.lower()
##    return Name
##
##>>> L1 = ['adam', 'LISA', 'barT']
##>>> L2 = list(map(normalize, L1))
##>>> print L2
##['Adam', 'Lisa', 'Bart']
##>>> from functools import reduce
##>>> def prod(L):
##	def fn(x,y):
##		return x*y
##	result = reduce(fn, L)
##	return result
##
##>>> prod([3,5,7,9])
##945
