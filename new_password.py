from random import randint

def new_password(words):
    d = dict()
    with open('eff_large_wordlist.txt', encoding='utf-8') as file:
        for line in file:
            lst = line.split()
            d[str(lst[0])] = lst[1]

    passphrase = ''
    
    # roll 5 dice to get a code words number of times
    for i in range(words):
        code = ''
        for j in range(5):
            code = code + str(randint(1,6))
        passphrase = passphrase + d[code] + ' '

    return passphrase.rstrip()

print(new_password(4))
    
    
