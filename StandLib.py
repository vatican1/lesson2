import sys


def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items:
                show_sizeof(xx, level + 1)
            else:
                for xx in x:
                    show_sizeof(xx, level + 1)

d_letter= {}
d = {}
file = open('text.txt', 'r')
for line in file:
    line = line.rstrip()
    for words in line.split(' '):
        for letters in words:
            if d_letter.get(letters) != None:
                d_letter[letters] += 1
            else:
                d_letter[letters] = 1

        if d.get(words) != None:
            d[words] += 1
        else:
            d[words] = 1

max = 0
word = 'a'
for i in d:
    if d[i]>max:
        max = d[i]
        word = i
print(max, word)
max = 0
letter = 'a'
for i in d_letter:
    if d_letter[i]>max:
        max = d_letter[i]
        letter = i
print(max, letter)
