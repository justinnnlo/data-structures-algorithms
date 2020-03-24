def URLify(str, str_length):
    '''
        the function replaces single spaces with %20 and remove spaces at the end
    '''
    # str.strip removes the front and back spaces of the str
    str = str.strip()
    print('after stripping spaces front n back: ', str)
    char_list = []

    for char in list(str):
        if char == ' ':
            char_list.append('%')
            char_list.append('2')
            char_list.append('0')
        else:
            char_list.append(char)
    print(''.join(char_list))
    return ''.join(char_list)


print(URLify('much ado about nothing      ', 22))
print(URLify('Mr John Smith    ', 13))
