def computepay(h,r):
    if (h>40):
        x = (h-40)*r*1.5
        p = (40*r)+x
    else :
        p = h*r
    return p

hrs = input("Enter Hours:")
rat = input("Enter Rates:")
p = computepay(float(hrs),float(rat))
print("Pay",p)
