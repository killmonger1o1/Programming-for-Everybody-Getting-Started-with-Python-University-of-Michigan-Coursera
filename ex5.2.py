l = None
s = None
while True:
    x = input("enter the number: ")
    if x == 'done':
        break
    else :
        try :
            x = float(x)
        except :
            print('Invalid input')
            continue
        if l is None:
            l = x
        elif l<x :
            l = x

        if s == None:
            s = x
        elif s > x :
            s=x
def op(l,s):
    print ('Maximum is',int(l))
    print ('Minimum is',int(s))

op(l,s)
