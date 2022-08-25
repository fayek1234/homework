
a = int(input('Enter first number a: '))
b = int(input('Enter second number b: '))
c = int(input('Enter third number c: '))


a = 15
b = 40
c = 150

def max(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


print(max(a, b, c))