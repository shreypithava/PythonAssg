import hashlib
import random
#
# d = {}
# d['208f1a0c208342372b75d914b6c098d626becf07'] = "0x1F4"
# d['61fc7fbf6b24ff258633dad73f13f9bd66a2477f'] = "0x1E240"
# d['8a57a79d7a9921cd2344e7295dc72359780e9f9d'] = "0x1DADF"
# d['bba1db3a9d5ba9f72b91312e730a9612dfdea053'] = "0x1e240"
# d['350d5bf1074e5557367a24ae9e07ab65aacfc031'] = "0xd9038"
#
#
# here is an example on how to use hashlib
counter = 0
while True:
    length = random.randint(5, 10)
    value = ''
    for i in range(length):
        value += chr(random.randint(97, 122))
    if hashlib.sha1(value.encode('utf-8')).hexdigest()[:4] == '6808':
        counter += 1
        print(value)
        if counter == 5:
            break
# value = "oldschool"
# value = value.encode("utf-8")
# print(hashlib.sha1(value).hexdigest())
#
#
# def bruteforce():
#     # here goes your code but this function should be never called on the
#     # system here
#     dict_list = []
#
#     for i in d.keys():
#         dict_list.append(i)
#
#     value_list = []
#     for i in range(1000000):
#         valhex = temp = str(hex(i))
#         valhex = valhex.encode("utf-8")
#         if hashlib.sha1(valhex).hexdigest() in dict_list:
#             value_list.append(i)
#         valhex_upper = temp[:2] + temp[2:].upper()
#         valhex_upper = valhex_upper.encode("utf-8")
#         if hashlib.sha1(valhex_upper).hexdigest() in dict_list:
#             value_list.append(i)
#     return sorted(set(value_list))
#
#
# def get_hash_dict():
#     global d
#     return d
#
#
# # abc = hex(2)
# # print(abc)
#
#
# # for k in d.items():
# #     print(k[1])
#
# def get_integer_values():
#     returnlist = []
#     for value in d.values():
#         number = 0
#         for i in range(len(value[2:])):
#             item = value[len(value) - i - 1]
#             if item == 'a' or item == 'A':
#                 number += (16 ** i) * 10
#             elif item == 'b' or item == 'B':
#                 number += (16 ** i) * 11
#             elif item == 'c' or item == 'C':
#                 number += (16 ** i) * 12
#             elif item == 'd' or item == 'D':
#                 number += (16 ** i) * 13
#             elif item == 'e' or item == 'E':
#                 number += (16 ** i) * 14
#             elif item == 'f' or item == 'F':
#                 number += (16 ** i) * 15
#             else:
#                 number += (16 ** i) * int(item)
#         returnlist.append(number)
#     returnlist = sorted(set(returnlist))
#     print(type(returnlist))
#     return returnlist
#
#
# print(get_integer_values())
