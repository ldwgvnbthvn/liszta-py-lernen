
# PROMPT: Temperature converter

def fahrenheit_to_celsius(temp):
    cels = (temp - 32)/1.8
    return cels


def celsius_to_fahrenheit(temp):
    fahr = (temp*1.8) + 32
    return fahr

print(fahrenheit_to_celsius(257))
print(celsius_to_fahrenheit(125))
