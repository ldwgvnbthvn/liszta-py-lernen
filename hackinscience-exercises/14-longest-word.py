
# = PROMPT: Write a function giving the longest word in a given text.

text = "Monty Python and the Holy Grail"

def longest_word(text):
    length = 0
    longest = 0
    listw = text.split()
    if listw == []:
        return
    nword = len(listw)
    for i in range(nword):
        length = len(listw[i])
        if length > longest:
            longest = length
            global lw
            lw = listw[i]
    return lw

print(longest_word(text))