
'''
Once upon a time, in Paris, the city of romance, Bob and Alice met and fall in love with each other.

EXERCISE 1
To fullfill their romance, they want to meet as much as possible. 
They share their daily paths among Paris districts to know where they can find each other at the same place.
As you know there is 20 districts in Paris:
{"Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "ⅩⅠ", "ⅩⅡ", "ⅩⅢ", "ⅩⅣ", "ⅩⅤ", "ⅩⅥ", "ⅩⅦ", "ⅩⅧ", "ⅩⅠⅩ", "ⅩⅩ"}
Make a function that returns a set of the districts they both visit during the day.

EXERCISE 2
Time goes on, and love goes by...
Alice is bored and get a crush for the strong and handsome Silvester.
In order to have an affair with Silvester she must find out where both Silvester and her go during the day.
But to avoid an unfortunate encounter with Bob, she must be sure Bob doesn't go there also.
Make a funtion that returns a set of all places where Alice and Silvester can meet and be sure Bob won't be.
'''
# Daily paths of every person
alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']

bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']

silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

# EXERCISE 1
def love_meet(bob, alice):
    lalice = set(alice)
    lbob = set(bob)
    meet = lalice & lbob
    return meet
    
print("Where Bob and Alice can meet: ", love_meet(bob,alice))
                            
# EXERCISE 2
def affair_meet(bob, alice, silvester):
    lalice = set(alice)
    lbob = set(bob)
    lsil = set(silvester)
    
    inter = lalice & lsil
    nobob = inter - lbob
    return nobob

print("Where Alice and Silvester can meet, without Bob: ", affair_meet(bob, alice, silvester))
print("Bob doesn't deserve her :(")