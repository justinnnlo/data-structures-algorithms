def string_compression(input_string):
    # takes care of upper and lower case -> all to lower
    # example: given aabcccccaaa shoud return -> a2b1c5a3
    input_string = input_string.lower()
    count = 1
    # string that is used to store the compressed string
    compressed_str = ""
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            count += 1
        else:
            compressed_str += input_string[i] + str(count)
            count = 1
    print(i)
    print(input_string[i])
    print(count)
    compressed_str += input_string[i] + str(count)

    if len(compressed_str) >= len(input_string):
        return input_string
    else:
        return compressed_str


print(string_compression('aabcccccaaa'))
