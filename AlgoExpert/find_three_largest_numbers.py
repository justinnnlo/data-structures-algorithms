def find_three_largest_numbers(array):
    largest_three = [None, None, None]
    for num in array:
        update_largest(largest_three, num)
    return largest_three


def update_largest(largest_three, num):

    if largest_three[2] is None or num > largest_three[2]:
        shift_and_update(largest_three, num, 2)
    elif largest_three[1] is None or num > largest_three[1]:
        shift_and_update(largest_three, num, 1)
    elif largest_three[0] is None or num > largest_three[0]:
        shift_and_update(largest_three, num, 0)


def shift_and_update(arr, num, idx):
    for i in range(idx + 1):
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i+1]


print(find_three_largest_numbers([10, 5, 9, 10, 12]))
