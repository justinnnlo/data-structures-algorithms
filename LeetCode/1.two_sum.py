# classic solution


def two_sum(nums, target):
    cache = {}

    for i in range(len(nums)):
        num = nums[i]
        match = target - num
        if match in cache.keys():
            return [cache[match], i]
        else:
            cache[num] = i
    return


print(two_sum([2, 7, 11, 15], 9))
