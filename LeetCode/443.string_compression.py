def string_compression(chars_arr):
    charsArrLen = len(chars_arr)
    idx, count = 0, 1

    for j in chars_arr:
        if j < charsArrLen and chars_arr[j] == chars_arr[j - 1]:
            count += 1
        else:
            chars_arr[i] = chars_arr[j - 1]
            # move idx pointer to right by 1
            idx += 1
            if count > 1:
                for digit in str(count):
                    chars_arr[i] = digit
                    i += 1
    # idx is at the new length of compresed arr -> so return idx
    return idx
