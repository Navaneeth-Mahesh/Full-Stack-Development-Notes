#Armstrong Number or Not

n = int(input("Enter the Number :"))
s = 0
num = n 
while (n > 0 ):
    r = n%10
    s = s+(r**3)
    n = n/10 
    if(s == num):
        print("the number is Armstrong")
    else: 
        print("the number is not armstrong ")