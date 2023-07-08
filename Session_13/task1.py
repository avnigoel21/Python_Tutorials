#Write a program using functions to convert celsius to fahrenheit

# (0°C × 9/5) + 32 = 32°F


# cel  = 5°C

def farh(cel):
    return (cel * (9/5)) + 32 

c = 0
f = farh(c)
print("Fahreheit Temp is : " + str(f))