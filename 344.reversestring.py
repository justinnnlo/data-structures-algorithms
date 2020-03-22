# swapping in place -> hence nothing to return
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[-i - 1] = s[-i - 1], s[i]
    # return s


print(reverseString(["h", "e", "l", "l", "o"]))
