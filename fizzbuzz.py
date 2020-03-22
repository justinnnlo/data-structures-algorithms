def fizz_buzz(num):
    fizzbuzzlist = []
    if num is None:
        raise TypeError('num cannot be none')
    if num < 1:
        raise ValueError('num cannot be less than one')
    for i in range(1, num + 1): 
        if i%3 == 0 and i%5 == 0:
            fizzbuzzlist.append('FizzBuzz')
        elif i%3 == 0:
            fizzbuzzlist.append('Fizz')
        elif i%5 == 0:
            fizzbuzzlist.append('Buzz')
        else:
            fizzbuzzlist.append(str(i))
    return fizzbuzzlist

print(fizz_buzz(15))