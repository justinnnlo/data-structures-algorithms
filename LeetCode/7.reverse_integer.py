''' 
- Given a 32-bit signed integer, reverse digits of an integer. 

Example 1: Input: 123 -> Output: 321

Example 2: Input: -123 -> Output: -321

Example 3: Input: 120 -> Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


def reverse_integer(number):
    reversed_int = int(str(abs(number))[::-1])

    if reversed_int > 2 ** 31 - 1 or number == 0:
        return 0

    return reversed_int * - 1 if number < 0 else reversed_int


print(reverse_integer(123))
print(reverse_integer(321))
print(reverse_integer(120))
print(reverse_integer(-123))
