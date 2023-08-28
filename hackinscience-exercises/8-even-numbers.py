
# PROMPT: Write a function printing every even numbers in the given range, one number per line.
# Your function have to be named even_numbers and accept two parameters named start and stop.
    

def even_numbers(start, stop):
    for i in range (start, stop):
        sisa = i % 2
        if sisa == 0:
            print(i)

print(even_numbers(0,10))