"""
try:
    with open('test2.txt', 'a') as file:
        file.writelines(["\nTESTING 1: ", "\nTESTING 2: "])
except FileNotFoundError as e:
    print("ERROR", e)
"""


with open('test.txt', 'r') as file:
    lines = file.readline()
    print(lines)


"""
with open('test.txt', 'r')as file:
    Lines = file.readlines()
    print(len(Lines))
    for line in Lines:
        print(line)
"""