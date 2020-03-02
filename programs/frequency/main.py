from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyzäöüß'
chars_to_remove = '.,?!-–:;()*'

def trim_to_word(word):
    for cr in chars_to_remove:
        word = word.replace(cr, "")
    return word

f = open("feb262020.txt", "r")

if f.mode == 'r':
    contents = f.read()

contents = contents.lower()
contents = contents.split()
contents = [trim_to_word(word) for word in contents]
frequency_pairs = Counter(contents).most_common()
# print(frequency_pairs)

for w in frequency_pairs:
    print(w[0], w[1])