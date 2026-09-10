neg = pos = zeroes = 0
print("enter -1 to exit..")
while(1):
    num = int(input("enter any number :"))
    if(num == -1):
        break
    if(num == 0):
        zeroes = zeroes + 1
    elif(num > 0):
        pos = pos + 1
    else:
        neg = neg + 1
print("Count of pos numbers entered :", pos)
print("Count of neg numbers entered :", neg)
print("Count of zeroes entered : ", zeroes)