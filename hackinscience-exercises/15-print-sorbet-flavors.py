'''
PROMPT: Provide a script printing every possible sorbet duos from a given list of flavors.
Don't print recipes with twice the same flavor (no "Chocolate Chocolate"), 
and don't print twice the same recipe (if you print "Vanilla Chocolate", don't print "Chocolate Vanilla", or vice-versa).
'''

# List of the flavors
f = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

def pair_flavor():
    pair = ["null","null"]
    for x in range(7):
        pair[0] = f[x]
        for y in range(7):
            if y>x:
                pair[1] = f[y]
                print(pair[0],pair[1], sep=", ")
                
pair_flavor()