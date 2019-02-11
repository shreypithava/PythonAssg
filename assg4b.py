# This is a program that I wrote and ran on my machine
# Note, for submisimport randomsion, please delete this part
import random


arg = []
for i in range(97, 123):
    strA = 'abcd' + chr(i)
    arg.append(strA)
    while True:
        strB = list(strA)
        random.shuffle(strB)
        if ''.join(strB) not in arg:
            arg.append(''.join(strB))
            if 97 <= i <= 100 and len(arg) % 60 == 0:
                break
            elif len(arg) % 120 == 0:
                break

for value in arg:
    random.seed(value)
    for x in range(10000):
        y = random.random()
        if y == 0.5799050747265982:
            print(value)
            print(y)
            print(random.random())
            print(random.random())
            print(random.random())
            print(random.random())
            break

# Valid seed
# 0.5799050747265982
# 0.44127068094893274
# 0.5895715579291188
# 0.23206666986379954
# 0.8205361742093551
