
# x = 5371
# x1 = x + 1
# xStr = str(x1)

# digits = [None] * len(xStr)

# index = 0

# for i in xStr:
#     digits[index] = i
#     index += 1

# print(digits)


digits = [5, 3, 6, 1]

for i in range(len(digits) -1, -1, -1):
    digits[i] += 1
    return digits

