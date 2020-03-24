# swapping in place -> hence nothing to return
# python way of swapping is so much better than the javascript way


def reverse_string(s):
    """
    Do not return anything, modify s in-place instead.
    """
    # for i in range(len(s) // 2):
    #     s[i], s[-i - 1] = s[-i - 1], s[i]
    # return s

    # 2 pointer swap method
    start, end = 0, len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


print(reverse_string(["h", "e", "l", "l", "o"]))
