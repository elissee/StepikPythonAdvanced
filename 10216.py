letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_dict = dict(zip(letters, morse))

s = input()

a = list(s.upper())
b = []

for letter in a:
    for key, value in morse_dict.items():
        if letter == key:
            b.append(value)

for i in b:
    print(i, end=' ')
