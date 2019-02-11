def caesar_chiper_encrypt(text, rot=5, *args):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for letter in text:
        if letter not in letters and letter != ' ':
            return 'error'
    text2 = ''
    text1 = text
    if len(args) != 0:
        for tup in args:
            oldletter = tup[0].lower()
            newletter = tup[1].lower()
            for letter in text1:
                if letter == oldletter:
                    text2 += newletter
                elif letter == newletter:
                    text2 += oldletter
                else:
                    text2 += letter
            text1 = text2
        print(text2)
        text = text2[len(text2) - len(text):]

    ciphertext = ''
    for letter in text:
        if letter != ' ':
            character_number = letters.index(letter) + rot
            if character_number >= len(letters):
                character_number -= len(letters)
            elif character_number < 0:
                character_number += len(letters)
            ciphertext += letters[character_number]
        else:
            ciphertext += ' '
    return ciphertext


print(caesar_chiper_encrypt('abc', 1, ('c', 'a'), ('b', 'd'), ('f', 'g')))
