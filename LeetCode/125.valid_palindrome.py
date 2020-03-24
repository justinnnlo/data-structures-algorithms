def is_palindrome(s):
    if s == '':
        return True
    left, right = 0, len(s) - 1
    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        elif s[left].isalum():
            right -= 1
        else:
            left += 1
    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
