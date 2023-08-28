
# PROMPT: Find the sum of all natural numbers below 1000 (<1000) that are multiples of 3 or 5

start = 0
stop = 1000


def multi(start,stop):
    sum = 0
    for i in range(start, stop):
        tri = i%3
        funf = i%5
        if tri == 0 or funf == 0:
            sum = sum + i
    return sum
    
print(multi(start,stop))