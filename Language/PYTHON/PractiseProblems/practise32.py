"""
coffee = ['milk', 'water', 'sugar']
def reverse(str): 
    return str[::-1]
reversed_coffee = map(reverse, coffee)
for x in reversed_coffee:
    print(x)
"""
"""
a = [[96], [69]]
print(''.join(list(map(str, a))))
"""
"""
z  = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)
"""
"""
def summation(n):
    if n == 1:
        return 0
    return n + summation(n-1)

a = summation(5)
print(a)
"""

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
    return numbers < 50
small = list(map(lesser, numbers))
print(small)
