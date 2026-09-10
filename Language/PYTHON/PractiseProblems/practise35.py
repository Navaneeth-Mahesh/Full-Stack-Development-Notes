"""
def f():
    global str
    print(str) 
    str = "Hello Navaneeth!!" #then this !!
    print(str)
str = "Welcome, Home!"   #this prints first
f()
"""
"""
def display(str):
    print(str)
x = display("Hello, Navaneeth!!!") #display(str) => display("Hello, Navaneeth!!!")
print(x)

print(display("welcome, Home"))

#output 

#Hello, Navaneeth!!!
#None
#welcome, Home
#None

"""
"""
def cube(x):
    return (x*x*x)
num = 1000
result = cube(num)
print('cube of', num,' = ', result)

#output => cube of 1000 = 1000000000

"""

