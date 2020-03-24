# the approach is to add another copy of strA to strA and check to see if strB is in strA
# because if you do A + A e.g. strA = 'abcde' strB = 'cdeab'
# A + A = 'abcdeabcde'
#    strB = 'cdeab'


def rotate_string(strA, strB):
    ''' 'waterbottle' is a rotation of 'erbottlewat' '''
    if len(strA) != len(strB):
        return False
    strA = strA + strA
    return strB in strA


print(rotate_string('abcde', 'cdeab'))
