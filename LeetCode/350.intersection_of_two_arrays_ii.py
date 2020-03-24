def intersection(list1, list2):
    d = {}
    res = []
    for n in list1:
        if d[n] is None:
            d[n] = 1
        else:
            d[n] += 1
    # while there are still things to be popped
    while list2:
        ele = list2.pop()
        if ele in d and d[ele] > 0
        res.append(ele)
        d[ele] -= 1
    return res
