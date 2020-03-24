def string_compression(chars_arr):
    charsArrLen = len(chars_arr)
    i, count = 0, 1

    for j in range(1, charsArrLen + 1):
        if j < charsArrLen and chars_arr[j] == chars_arr[j - 1]:
            count += 1
        else:
            chars_arr[i] = chars_arr[j - 1]
            # move idx pointer to right by 1
            i += 1
            if count > 1:
                for digit in str(count):
                    chars_arr[i] = digit
                    i += 1
    # idx is at the new length of compresed arr -> so return idx
    return i


print(string_compression(["a", "b", "b", "b", "b",
                          "b", "b", "b", "b", "b", "b", "b", "b"]))
