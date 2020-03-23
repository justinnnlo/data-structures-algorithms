# try to implement this algorithm without using an extra data structure

# not the optimized solution since I used extra space here


# def isUnique(str):
#     cache = {}

#     str = str.lower()
#     str = str.replace(' ', '')

#     for char in str:
#         if not char in cache:
#             cache[char] = True
#         elif char in cache:
#             return False
#     return True

# optimized solution with no extra space


def isUnique(str):
    if len(str) == len(set(str)):
        return True
    return False


print(isUnique('hello'))
print(isUnique('MysTring'))
