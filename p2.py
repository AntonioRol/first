def cubic(x):
    result = x*x*x
    return result

def cubic2(x):
    return x*x*x
value1 = cubic(3)
value2 = cubic(3)
print "value1 - ", value1
print "value2 - ", value2

def adder(n1,n2):
    return (n1+n2)
print "adder - ",adder(10, 1)
def avg_three(n1,n2,n3):
    temp = n1+n2+n3
    return temp/3.0
print "avg 18, 23, 19-", avg_three(18, 23, 19)
print "avg 25, 35, 45,-", avg_three(25, 35, 50)