def secret(a):
    return a % 3 != 0 and a % 5 != 0
result = filter(secret, range(1, 31))
print(list(result))

# Output: [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29]
# 12 wont be printed because 12 % 3 == 0