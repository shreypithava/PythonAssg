def mod_exp_method(num, exp,
                   mod):  # parameters explained, if we wanted to find 3 ^ 200  mod 50, num = 3, exp = 200, mod = 50
    power_of_two = 2  # this variable is a power of two
    list_of_rem = [
        num % mod]  # is a list, stores the remainders, like for above example, it would have, 3, 9, 31, 11 and so on....
    while exp >= power_of_two:  # finds all the remainders and stops after 128 as 256 > 200
        rem = list_of_rem[len(
            list_of_rem) - 1] ** 2 % mod  # finds remainders by squaring the previous remainder and then applying mod
        list_of_rem.append(rem)
        power_of_two *= 2
    number = 1
    binary = str(bin(exp))  # finds binary number of 200(above example) and returns as string
    for i in range(len(binary)):  # goes through binary number to find 1
        if binary[len(binary) - i - 1] == '1':  # multiply if 1
            number *= list_of_rem[i]
    number %= mod  # take mode of that small number and return it
    return number


# please note that from here on, variable names speak for themselves
# whenever asked for input, directly enter after '=', no spaces or hitting enter before entering input
p = int(input("Enter prime number p="))

q = int(input("Enter prime number q="))
n = p * q
o = (p - 1) * (q - 1)  # totient function

e = int(input("Enter e="))
print(n)
d = 0
while d * e % o != 1:  # finding d
    d += 1

public_key = [d, n]  # this is public key
private_key = [e, n]  # this is private key
# print('Alice\'s secret key is {}'.format(private_key))
#
m = int(input("Enter message to encrypt="))
c = mod_exp_method(m, public_key[0], public_key[1])  # calls exponential function

M = mod_exp_method(c, private_key[0], private_key[1])  # calls exponential function

# print('\np={}\nq={}\nn={}\no(n)={}\ne={}\nd={}\nM={}\nC={}\nM\'={}'.format(p, q, n, o, e, d, m, c, M))  # prints every
# thing required
print('M={}\nC={}\nM\'={}'.format(m, c, M))
# print('Public key  = {}\nPrivate key = {}'.format(public_key, private_key))

# .format on line 37 works with replacment fields
# print('abc{}'.format(13))     # here it would print abc13, it directly replaces {}
# print('abc{}{}'.format(12, 13)) # here it would print abc1213

# please note that for the whole code to work, you must have version of python 3 or better
