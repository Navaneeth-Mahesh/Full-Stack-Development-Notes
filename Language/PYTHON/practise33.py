"""
def testing():
    print("testing is good")

x = testing()
print("hi navaneeth how is function testing going : ", x)
"""
"""
def bmi(weight, height):
    return weight /(height ** 2)

result = bmi(80, 5.7)
print(result)
"""
"""
def caluculate(add, subs):
    return add * 7 / ( subs - 2 )

result = caluculate(58, 7)
print(result)
"""


"""
def details(name, age, weight, height):
    print(name)
    print(age)
    print(weight)
    print(height)

def education(school, inter, engineering):
    print(school)
    print(inter)
    print(engineering)

person1 = details("nav", 19, 80, 5.8)
moredetails = education("ushodaya", "aditya", "pragati")
print(person1)
print(moredetails)

person2 = details("ravi", 20, 78, 5.9)
moredetails = education("aditya", "aditya", "aditya")
print(person2)
print(moredetails)

"""
"""
def add(x,y):
    return x  + y
a = 10 
b = 20
operation = add 
print(operation(a,b))
"""
"""
def func():
    for i in range(10):
        print("finiteloop")
func()
"""
"""
def foodlist(item1, item2):
    print(item1)
    print(item2)
order = foodlist("soda", "biryani")
def bill(tax, food_cost):
    print("tax :", tax)
    print("food_cost : ", food_cost)
    total = tax * food_cost
    return total

bill_amount = bill(0.5, 500)
print(bill_amount)
"""

"""
num1 = 10
print("Global varibale num1 = ", num1)

#function part *******
def func(num2):
    print("In function - local var num2 = ", num2)
    num3 = 30
    print("In function - local var num 3 = ", num3)
func(20)
#function ends here***********
print("num1 again = ", num1) 

"""


"""
var = "Good"
def show():
    global var1
    var1 = "Morning"
    print("In Function var is - " , var)
show()

print("out func, var1 is - ", var1)
print("var is  - ", var)
"""



