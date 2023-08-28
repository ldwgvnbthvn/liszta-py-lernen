
# PROMPT: Provide a script printing every possible pairs of two different letters.
# Only lower case, one pair per line, ordered alphabetically.
# Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...

import string

hitung = [x for x in range(26)]
awal = "aa"
list1 = list(awal)
pisah = string.ascii_lowercase

for x in hitung:
    list1[0] = pisah[x]
    for y in hitung:
        list1[1] = pisah[y]
        if list1[0] != list1[1]:
            gabung = "".join(list1)
            print(gabung)