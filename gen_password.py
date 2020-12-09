# random should not be used for security so we use secrets
import secrets

def generate_passphrase(nw):
    with open('eff_large_wordlist.txt', encoding='utf-8') as file:
        words = [line.split()[1] for line in file]

    passphrase = [secrets.choice(words) for i in range(nw)]
    return ' '.join(passphrase)

print(generate_passphrase(4))
