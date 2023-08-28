
# PROMPT: Provide a script that prints the sum of every even numbers in the range [0; 100].

start = 0
stop = 102

def sum(start, stop):
    s = 0
    for i in range(start, stop):
        mod = i % 2
        if mod == 0:
            s = s + i
    return s

print(sum(start, stop))