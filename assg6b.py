import string

# supported alphabet
alphabet = string.ascii_letters + " " + "," + "-" + "!"
char = []
for alpa in alphabet:
    char.append(alpa)


# print(alphabet)


# decrypt function
# chiffer and key need to be hex arrays as this what my unit test will pass
# return value should be a string
def decrypt(chiffer):
    semi = chiffer.split(':')
    for key in range(256):
        answer = ''
        for i in semi:
            # print('{}'.format(chr(key ^ int(i, 16))), end='')
            if chr(key ^ int(i, 16)) in char:
                answer += chr(key ^ int(i, 16))
        print('{}\t\t{}'.format(answer, key))
        print('-' * 90)


# print('{}, {}'.format(chr(int(i, 16)), int(i, 16)))

# key = dict()
# counter = 0
# for b in semi:
#     for i in range(counter + 1, len(semi)):
#         if int(b, 16) ^ int(semi[i], 16) in key:
#             key[int(b, 16) ^ int(semi[i], 16)] += 1
#         else:
#             key[int(b, 16) ^ int(semi[i], 16)] = 1
#     counter += 1
# for i in key.items():
#     print(i)

# simply returns the decrypted message, nothing else
def return_message():
    return "the cleartext of the message"


# all other code that you need should go below here

a = '84:9a:8f:b2:df:bc:a5:9e:8a:a5:8d:c2:e0:96:88:e0:86:81:b5:df:8f:b2:9a:ce:a1:9d:82:a5:df:9a:af:df:9c:a5:9e:8a:e0' \
    ':8b:86:a9:8c:c2:e0:86:81:b5:df:9d:b5:9c:8d:a5:8c:9d:a6:8a:82:ac:86:ce:b3:90:82:b6:9a:8a:e0:8b:86:a5:df:8d:a8:9e' \
    ':82:ac:98:8b:a4:df:c3:ed:df:8c:a1:9b:ce:a1:8c:9d:e1'

decrypt(a)
