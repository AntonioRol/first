
from math import sqrt
def find_hypothenuse(a,b):
    a_square = a*a
    b_square = b*b
    result = sqrt(a_square + b_square)
    return result

print "hypothenuse 3, 4_", find_hypothenuse(3,4)

def print_name(name):
    print 'person name:-' + name

print_name('Jose')
print_name('Ned')

