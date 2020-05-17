hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates:")
r = float(rate)
if (h<=40):
    p=h*r
else:
    x=(h-40)*r*1.5
    p=(40*r)+x
print(p)
