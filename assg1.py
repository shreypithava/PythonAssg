# word = 'hello world'
#
# for i in range(len(word)):
#     print(word[len(word) - i - 1:])
# --------------------------------------------
# word = 'foobar'
# output = ''
# for i in range(len(word), 0, -1):
#     if word[i - 1] != 'o':
#         output += word[i - 1]
#         print(output)
#
# output1 = ''
# for i in range(len(word)):
#     if word[len(word) - 1 - i] != 'o':
#         output1 += word[len(word) - 1 - i]
#         print(output1)
counter = 0
a = [8, 5, 4, 7, 9, 3]
for i in range(len(a) - 1, 0, -1):
    for j in range(i):
        counter += 1
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
    print(a)
print(counter)
