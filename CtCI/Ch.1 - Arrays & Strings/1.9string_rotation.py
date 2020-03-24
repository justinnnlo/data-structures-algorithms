def string_rotation(strA, strB):
    if len(strA) != len(strB):
        return False
    strA = strA + strA

    if strB in strA:
        return True
    else:
        return False
