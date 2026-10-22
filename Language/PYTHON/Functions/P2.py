var = "Good"
def show():
    global var1
    var1 = "Morning"
    print("In function var is - ", var)
show()
print("Outside function, var1 is -", var1)
print("var is - ", var)