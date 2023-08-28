
# PROMPT:Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.
    
import string

hitung = [x for x in range(26)]
awal = "aa"
list1 = list(awal)
pisah = string.ascii_lowercase
#pisah = abcdefghijklmnopqrstuvwxyz

for x in hitung:
    list1[0] = pisah[x]
    for y in hitung:
        list1[1] = pisah[y]
        gabung = "".join(list1)
        print(gabung)
