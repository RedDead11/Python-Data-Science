# s = "abcabcbb"

# saving = []

# for i in range(len(s)-2):
#     if s[i] != s[i+1] and s[i+2]:

#         print(s[i], s[i+1])
#         current = s[i] + s[i+1]
#         saving += current

#         print("Saving = " + ", " .join(saving))


from turtle import *

color('red')


for i in range(20):
    forward(10)
    right(20)
    for j in range(1):
        color('blue')
        right(1)
