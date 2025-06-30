import time

word = 'Thank you for checking out my profile!'
amount = 1


def decrypt(letter, amount):

    a_ascii = ord('a')
    #true_code = a_ascii + (((letter - a_ascii) + amount) % 26)
    
    letter += amount
    decoded = chr(letter)
    return decoded

#print(decrypt('a', 2))

def decode_word(word, amount):
    passw = ''
    for item in word:
        letter = item
        n_letter = 'A'
        while n_letter != letter:
            n_letter = ord(n_letter)
            n_letter += 1
            if 32 > n_letter or 127 < n_letter:
                n_letter = 32
            n_letter = chr(n_letter)
            print(f'{passw + n_letter}')
            if n_letter == item:
                break
            time.sleep(0.005)
        passw += n_letter
    return passw   
    

#word = decrypt[('a', 2), ('b', 2)]
x = decode_word(word, 1)
for i in range(40):
    print(x)
