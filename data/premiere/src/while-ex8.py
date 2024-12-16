# FONCTIONS
def is_perfect(n):
    s = 0
    d = 1
    while d < n:
        if n % d == 0:
            s = s + d
        d = d + 1
    return s == n

# SCRIPT
print(is_perfect(6))
print(is_perfect(16))
print(is_perfect(28))

# n = 1
# keep_searching = True
# while keep_searching :
#     n = n + 1
#     if n % 2 == 1 and is_perfect(n):
#         keep_searching = False
# print(n)
