letterDict = dict()
with open('crypt.txt') as handle:
    for line in handle.readlines():
        for letter in line:
            if 97 <= ord(letter) <= 122:
                if letter in letterDict:
                    letterDict[letter] += 1
                else:
                    letterDict[letter] = 1

main_list = list()
for maxValue in sorted(letterDict.values(), reverse=True):
    for k, v in letterDict.items():
        if maxValue == v:
            main_list.append(k)

priority_char = 'etanoisrhldcumfpgwbykvjxqz'

priority_dict = dict()

for x in range(len(main_list)):
    priority_dict[main_list[x]] = priority_char[x]

with open('decrypt.txt', 'w') as decrypt_file:
    for line in open('crypt.txt').readlines():
        line1 = ''
        for letter in line.rstrip():
            if 97 <= ord(letter) <= 122:
                line1 += priority_dict[letter]
            else:
                line1 += letter
        print(line1, file=decrypt_file)
# d = dict()
# total = 0
# for value in letterDict.values():
#     total += int(value)
# for key, value in letterDict.items():
#     d[key] = round(int(value) / total, 3)
#
# print(d)
